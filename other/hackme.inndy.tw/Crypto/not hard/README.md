# not hard
Cipher = `Nm@rmLsBy{Nm5u-K{iZKPgPMzS2I*lPc%_SMOjQ#O;uV{MM*?PPFhk|Hd;hVPFhq{HaAH<`  
用 base85 decode 後得到 `b'IZGECR33IRXSA6LPOUQGW3TPO4QGEYLTMUZTEIDFNZRW6ZDJNZTT67I='`  
最後用 base32 decode 得到 `b'FLAG{Do you know base32 encoding?}'`
```Python
import base64
print(base64.b32decode(base64.b85decode('Nm@rmLsBy{Nm5u-K{iZKPgPMzS2I*lPc%_SMOjQ#O;uV{MM*?PPFhk|Hd;hVPFhq{HaAH<')))
```
