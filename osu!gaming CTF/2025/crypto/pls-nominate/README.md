# crypto/pls-nominate

by WoodMan

## Summary

> pls help me get the attention of bns by spamming this message to them pls pls pls

## Challenge Solving

```python
ns = [ ... ]
cs = [ ... ]
e = 5

def egcd(a, b):
    if b == 0:
        return (1, 0, a)
    x, y, g = egcd(b, a % b)
    return (y, x - (a // b) * y, g)

def modinv(a, m):
    try:
        return pow(a, -1, m)
    except TypeError:
        x, _, g = egcd(a, m)
        if g != 1:
            raise ValueError("no inverse")
        return x % m

def crt_combine(a1, n1, a2, n2):
    s, t, g = egcd(n1, n2)
    if g != 1:
        raise ValueError("moduli not coprime")
    inv = s % n2
    k = ((a2 - a1) * inv) % n2
    x = a1 + n1 * k
    return x % (n1 * n2), n1 * n2

def int_nth_root(x, n):
    if x < 0:
        raise ValueError("negative")
    if x == 0:
        return 0, True
    lo = 1
    hi = 1 << ((x.bit_length() + n - 1) // n + 1)
    while lo < hi:
        mid = (lo + hi) // 2
        p = pow(mid, n)
        if p == x:
            return mid, True
        if p < x:
            lo = mid + 1
        else:
            hi = mid
    root = lo - 1
    return root, pow(root, n) == x

def main():
    res = cs[0]
    mod = ns[0]
    for a, n in zip(cs[1:], ns[1:]):
        res, mod = crt_combine(res, mod, a, n)
    N = mod
    root, exact = int_nth_root(res, e)
    if not exact:
        for k in range(1, 1000001):
            val = res + k * N
            root, exact = int_nth_root(val, e)
            if exact:
                break
        else:
            raise SystemExit("no root found")
    m = root
    mb = m.to_bytes((m.bit_length() + 7) // 8, 'big')
    prefix = b"hello there can you pls nominate my map https://osu.ppy.sh/beatmapsets/2436259 :steamhappy: i can bribe you with a flag if you do: "
    idx = mb.find(prefix)
    if idx != -1:
        print(mb[idx + len(prefix):].decode('utf-8', errors='replace'))
    else:
        print(mb[-200:].decode('utf-8', errors='replace'))

if __name__ == "__main__":
    main()

```

## Flag

`osu{pr3tty_pl3453_w1th_4_ch3rry_0n_t0p!?:pleading:}`
