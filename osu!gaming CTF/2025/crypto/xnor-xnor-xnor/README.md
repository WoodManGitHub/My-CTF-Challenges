# crypto/xnor-xnor-xnor

by WoodMan

## Summary

> https://osu.ppy.sh/beatmapsets/1236927#osu/2573164

## Challenge Solving

```python
def xnor_gate(a, b):
    return 1 if a == b else 0

def str_to_bits(s):
    bits = []
    for x in s:
        bits += [(x >> i) & 1 for i in range(8)][::-1]
    return bits

def bits_to_str(bits):
    return bytes([sum(x * 2 ** j for j, x in enumerate(bits[i:i+8][::-1])) for i in range(0, len(bits), 8)])

def xnor(pt_bits, key_bits):
    return [xnor_gate(pt_bit, key_bit) for pt_bit, key_bit in zip(pt_bits, key_bits)]

enc_hex = "7e5fa0f2731fb9b9671fb1d62254b6e5645fe4ff2273b8f04e4ee6e5215ae6ed6c"
enc_bytes = bytes.fromhex(enc_hex)
enc_bits = str_to_bits(enc_bytes)

known_plain = b"osu{"
known_bits = str_to_bits(known_plain)

key_bits = []
for i in range(len(known_bits)):
    key_bits.append(xnor_gate(enc_bits[i], known_bits[i]))

key_bits_32 = key_bits[:32]

key_repeated = (key_bits_32 * ((len(enc_bits) // 32) + 1))[:len(enc_bits)]
flag_bits = xnor(enc_bits, key_repeated)
flag = bits_to_str(flag_bits)

print(f"Key (4 bytes): {bits_to_str(key_bits_32).hex()}")
print(f"Flag: {flag.decode()}")
```

## Flag

Key (4 bytes): `eed32a76`

`osu{b3l0v3d_3xclus1v3_my_b3l0v3d}`

