# JS Safe 6.0
在解的過程中只要加上另一位好友的 Payload 與註解一個 `if`，就可以取得 Flag  
後來參考別人的 Write-up 才解開題目，希望明年有辦法解開

## Summary
You stumbled upon someone's "JS Safe" on the web. It's a simple HTML file that can store secrets in the browser's localStorage. This means that you won't be able to extract any secret from it (the secrets are on the computer of the owner), but it looks like it was hand-crafted to work only with the password of the owner…

## Files Provided
- js_safe_6.html

## File Analysis
使用瀏覽器開啟後可以看到一個酷炫畫面，並告訴你應該怎麼使用
![](./images/homepage.png)
- Open the page in Chrome (the only supported browser)
- Open Dev Tools and type:
- anti(debug); // Industry-leading antidebug!
- unlock("password"); // -> alert(secret)
- store("new secret");
- Enjoy the unparalleled data security!!!!1

先依據畫面上的內容來分析 `.html` 檔案，因此我先去看相關的幾個函數是怎麼寫的

### Functions
#### anti(debug)
![](./images/anti_debug.png)
初次使用 VSCode 開啟會得到非常多的黃色方框，游標滑上去會看到這樣子的訊息
```
The character U+2003 is invisible. Adjust settings
```
這個雖然長的很像空白，但實際上是另一個字元。過去相關的題目也有出現

#### unlock
![](./images/unlock.png)
先檢查輸入是否符合 `/^CTF{([0-9a-zA-Z_@!?-]+)}$/`，再進入到 `check()`  
接下來的 encrypted 跟 decrypted 就不重要了

##### check()
![](./images/check.png)
定義於 [anti(debug)](#anti(debug)) 中

#### store
![](./images/store.png)
老實說這邊不太重要，畢竟題目說明也有提到 Flag 不在你電腦上

## Challenge Solving
### Escape Anti-Debugger
一開始我被兩個長度檢查擋下，導致我無法修改檔案中的任何內容
![](./images/anti_debugger_1.png)
![](./images/anti_debugger_2.png)

看起來第二個長度檢查與整個 HTML 檔案較為有關連，因此我先修改並使他永遠是 false，這樣我就可以隨意更改內容
![](./images/escape_anti_debugger.png)

改完重新整理後得到新的錯誤
> Refused to execute inline script because it violates the following Content Security Policy directive: "script-src 'sha256-P8konjutLDFcT0reFzasbgQ2OTEocAZB3vWTUbDiSjM=' 'sha256-eDP6HO9Yybh41tLimBrIRGHRqYoykeCv2OYpciXmqcY=' 'unsafe-eval'". Either the 'unsafe-inline' keyword, a hash ('sha256-nArgG/Kg8kEACs2owqJeoSo4GHMLDdMGC8GlH/i+HGg='), or a nonce ('nonce-...') is required to enable inline execution.

依據錯誤訊息，將 `Content-Security-Policy` 兩個 sha256 刪除並修改為
```html
<meta http-equiv="Content-Security-Policy" id="c" content="script-src 'unsafe-inline' 'unsafe-eval'">
```

重新整理並依照題目要求的操作測試，發現能夠正常運作，現在我可以隨意修改檔案內容並進行各種測試與分析  
但 Console 一直被覆蓋與清除有點煩因此我把下面兩行註解，讓 Console 變乾淨
```javascript
...
// console.clear();
// console.log(content);
...
```

## References
- [kalmarunionen/NicolaiSoeborg CTF Writeup](https://github.com/NicolaiSoeborg/ctf-writeups/blob/master/2025/Google%20CTF%202025/README.md)
  - 這一個 Write-up 提點了我很多，也讓我知道缺少了什麼部分