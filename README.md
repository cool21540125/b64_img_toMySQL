# 把 圖片 塞到 MySQL
- 2018/08/09


```ps
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.19, for Win64 (x86_64)

$ python -V
Python 3.6.1 :: Anaconda 4.4.0 (64-bit)
```



# 前端作法

```html
<img id="demo" src="" alt="Picture GG">

<script>
    $(function() {
        $.ajax({
            url: '/api/logo/',
            type: 'GET',
        }).done(function(data, _, _) {
            $('#demo').attr('src', 'data:image/png;base64, ' + data['logo']);
        });
    });
</script>
```
