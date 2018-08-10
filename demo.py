import base64
import pymysql

DB_CONFIG = {
    'host': 'localhost',
    'user': '帳號~~~',
    'password': '密碼~~~',
    'db': 'pic',
    'charset': 'utf8'
}

with open('demo.png', 'rb') as f:
    mm = base64.b64encode(f.read())

conn = pymysql.Connect(**DB_CONFIG)


### 塞圖片到 MySQL
# with conn.cursor() as c:
#     c.execute("INSERT INTO `img` VALUES (%s)", (mm,))
#     conn.commit()


### 從 MySQL 撈出圖片
with conn.cursor() as c:
    c.execute("SELECT * FROM `img`")
    qq = c.fetchone()[0]
