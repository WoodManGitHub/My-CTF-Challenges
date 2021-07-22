# Weird Email 
```
Oops, this email has been modified,
But secret still there,
Can you find it?
```

用 Mail 軟體打開，看到底下有段 SCIST{ 開頭的文字  
轉換成 html 後得到 Flag  
然後我就在這邊卡了 30 分鐘  
Hint: 
- FLAG match regex ^SCIST{[^_=}]+}$
- FLAG contains some space, you shouldn’t remove it.

是的，你必須把 _ 換成空白
