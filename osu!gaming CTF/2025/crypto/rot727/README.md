# crypto/rot727

by WoodMan

## Summary

> i rotated my flag 727 times! that's super secure right
> `aeg{at_imuf_nussqd_zgynqd_paqezf_yqmz_yadq_eqogdq}`

## Challenge Solving

```python
def rot14(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 14) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 14) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

encrypted = "aeg{at_imuf_nussqd_zgynqd_paqezf_yqmz_yadq_eqogdq}"
decrypted = rot14(encrypted)
print(decrypted)
```

## Flag

`osu{oh_wait_bigger_number_doesnt_mean_more_secure}`

