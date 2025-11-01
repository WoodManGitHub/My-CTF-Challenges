# crypto/linear-feedback

by WoodMan

## Summary

> this owc map is so fire btw :steamhappy: https://osu.ppy.sh/beatmapsets/2451798#osu/5355997

## Challenge Solving

```python
from z3 import *
from hashlib import sha256

target_bits = [0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0]
ciphertext = bytes.fromhex("9f7f799ec2fb64e743d8ed06ca6be98e24724c9ca48e21013c8baefe83b5a304af3f7ad6c4cc64fa4380e854e8")

solver = Solver()
L1_initial = [Bool(f'L1_{i}') for i in range(21)]
L2_initial = [Bool(f'L2_{i}') for i in range(29)]

def clock(state, taps):
    fb = state[taps[0]]
    for t in taps[1:]:
        fb = Xor(fb, state[t])
    return state[0], state[1:] + [fb]

def xnor(a, b):
    return Not(Xor(a, b))

L1_state, L2_state = L1_initial[:], L2_initial[:]
L1_taps, L2_taps = [2,4,5,1,7,9,8], [5,3,5,5,9,9,7]

for i in range(72):
    b1, L1_state = clock(L1_state, L1_taps)
    b2, L2_state = clock(L2_state, L2_taps)
    solver.add(xnor(b1, b2) == BoolVal(target_bits[i]))

while solver.check() == sat:
    m = solver.model()
    k1 = int(''.join(['1' if m[v] else '0' for v in L1_initial]), 2)
    k2 = int(''.join(['1' if m[v] else '0' for v in L2_initial]), 2)

    ks = sha256((str(k1)+str(k2)).encode()).digest()*2
    flag = bytes([c ^ k for c, k in zip(ciphertext, ks)])
    if flag.startswith(b"osu{"):
        print(flag.decode())
        break

    solver.add(Or([v != m[v] for v in L1_initial+L2_initial]))
```

## Flag

`osu{th1s_hr1_i5_th3_m0st_fun_m4p_3v3r_1n_0wc}`

