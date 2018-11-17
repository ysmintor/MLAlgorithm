#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "88&aswott", "UCIDataSet")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "INSERT INTO LDPA (`sequence_name`, `tag`, " \
      "`timestamp`, `date`, `x_coordinate`, `y_coordinate`, `z_coordinate`, `activity`) " \
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

val = ('A06','010-000-024-033', '633790226051280329', '27.05.2009 14:03:25:127', 4.062931060791016, 1.8924342393875122, 0.5074254274368286,'talking')

dict = []
with open('/Users/york/Downloads/ConfLongDemo_JSI.txt') as f:
    for line in f.readlines():
        line_arr = line.strip().split(',')
        dict.append(tuple(line_arr))

# cursor.execute(sql, val)

cursor.executemany(sql, dict)
db.commit()

print(cursor.rowcount, "record inserted.")

# 关闭数据库连接
db.close()