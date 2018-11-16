#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "88&aswott", "UCIDataSet")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "INSERT INTO IHEPC (`date`, `time`, " \
      "`global_active_power`, `global_reactive_power`, `voltage`, `global_intensity`, `sub_metering_1`, `sub_metering_2`, `sub_metering_3`) " \
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

dict = []
with open('/Users/york/Downloads/household_power_consumption.txt') as f:
    for line in f.readlines():
        line_arr = line.strip().split(';')
        if not '?' in line_arr:
            dict.append(tuple(line_arr))

# cursor.execute(sql, val)

cursor.executemany(sql, dict)
db.commit()

print(cursor.rowcount, "record inserted.")

# 关闭数据库连接
db.close()