#  Linebot

# 特殊功能

+ 猜拳 [剪刀/石頭/布]
+ 新聞 
+ 幹話

example:
```c=
市長 猜拳 剪刀
```
```c=
市長 新聞
```

+ 備註:bbc似乎改了網頁所以不能用，但另一個神祕功能還可以 

# 學習
format
```c=
市長@[問題]@[回答]
```
example:
```c=
市長@你好@高雄市民好
```

# 成果
![](https://i.imgur.com/3950GEt.png)

# 打包
1. 創建config.py在資料夾內
2. 裡面打上
```
line_token = [你的token]
line_secret = [你的secret]
```
3. 丟到heroku

