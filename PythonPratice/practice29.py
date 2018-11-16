#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "88&aswott", "UCIDataSet")





# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "INSERT INTO IHEPC (`date`, `time`, " \
      "`global_active_power`, `global_reactive_power`, `voltage`, `global_intensity`, `sub_metering_1`, `sub_metering_2`, `sub_metering_3`) " \
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


# 建表依然存在问题，但直接放到 MySQL 语句中却能够执行，后面有时间来处理这个问题
create_sql = """
DROP TABLE IF EXISTS `IHEPC`;
CREATE TABLE `IHEPC`(
`id` INT,
`date` DATE, 
`time` TIME, 
`global_active_power` FLOAT, 
`global_reactive_power` FLOAT, 
`voltage` FLOAT , 
`global_intensity` FLOAT , 
`sub_metering_1` FLOAT , 
`sub_metering_2` FLOAT , 
`sub_metering_3` FLOAT 
)
"""
dict = []
with open('/Users/york/Downloads/household_power_consumption.txt') as f:
    for line in f.readlines():
        line_arr = line.strip().split(';')
        if not '?' in line_arr:
            line_arr[0] = "{2}-{1}-{0}".format(*line_arr[0].split('/'))
            dict.append(tuple(line_arr))

# cursor.execute(sql, val)

cursor.executemany(sql, dict)
db.commit()

print(cursor.rowcount, "record inserted.")

# 关闭数据库连接
db.close()