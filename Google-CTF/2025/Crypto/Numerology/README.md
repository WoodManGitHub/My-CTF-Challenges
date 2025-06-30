# Numberology
這次唯一解開的題目，能力不足QQ

## Summary
We were given a custom stream cipher, a known key, a fixed plaintext, many ciphertext pairs with known nonces and counters, and a target ciphertext (the flag) encrypted under unknown nonce/counter. The goal was to decrypt the flag.

## Files Provided
```
numerology
├── __pycache__
│   └── crypto_numerology.cpython-312.pyc
├── ctf_challenge_package.json
├── flag.txt
├── init.sh
└── readme.md
```

## File Analysis
- crypto_numerology.cpython-312.pyc
  - Python 編譯後的 bytecode
    - 可以 decompile 出原始碼
- ctf_challenge_package.json
  - 題目提供的 plaintext/chiphertext pair, key 與加密後的 flag
- flag.txt
  - 範例 flag
- init.sh
  - 題目的腳本
- readme.md
  - 題目說明

## Challenge Solving
### Decompile
題目提供了一個 `.pyc` 檔案，可以利用工具對檔案進行 Decompile。  
一開始使用 [uncompyle6](https://github.com/rocky/python-uncompyle6)，但發現不支援。
```
Unsupported Python version, 3.12.0, for decompilation
# Unsupported bytecode in file crypto_numerology.cpython-312.pyc
# Unsupported Python version, 3.12.0, for decompilation
```
於是轉往尋找其他工具，發現一個線上工具 [pylingual.io](https://pylingual.io/) 可以成功 Decompile。

### Analyze
針對 Decompile 後的原始碼進行分析，可以發現他是一個 [ChaCha20](https://cr.yp.to/chacha.html) 的改造版本。  
1. 正常 ChaCha20 會跑 20 輪，在這邊變異成 1 到 8 輪
```python
if not 1 <= rounds_to_execute <= 8:
  raise ValueError('rounds_to_execute must be between 1 and 8 for this modified version.')
```
2. 使用了一組固定的常數 `CHACHA_CONSTANTS`
```python
CHACHA_CONSTANTS = (1634760805, 857760878, 2036477234, 1797285236)
```
3. 與 ChaCha20 一樣，最後會輸出 64 bytes 的 keystream，拿去 XOR 做加解密。
```python
for i in range(16):
    state[i] = add32(state[i], initial_state_snapshot[i])
return words_to_bytes(state)
```

好累剩下再補