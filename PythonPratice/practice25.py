#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "88&aswott", "UCIDataSet")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "INSERT INTO customers (`name`, `address`) VALUES (%s, %s)"
val = ("Tim", "Highway 22")
cursor.execute(sql, val)

db.commit()

print(cursor.rowcount, "record inserted.")
# 关闭数据库连接
db.close()