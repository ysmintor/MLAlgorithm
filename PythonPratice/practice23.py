#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "88&aswott", "UCIDataSet")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

cursor.execute("SELECT * FROM LDPA")
result = cursor.fetchall()
for x in result:
    print(x)
# 关闭数据库连接
db.close()