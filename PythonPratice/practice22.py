#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "88&aswott", "UCIDataSet")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


sql = """INSERT INTO LDPA('Sequence Name', 'Tag identificator', 
'timestamp', 'date FORMAT', 'x coordinate', 
'y coordinate', 'z coordinate', 'activity') VALUES('A02',
         '010-000-024-033', 633790226051280329, 27.05.2009 14:03:25:127, 
         4.062931060791016, 1.8924342393875122,0.5074254274368286,'walking')"""

try:
    # cursor.execute(sql)
    # db.commit()

    cursor.execute("SELECT * FROM LDPA")
    resultes = cursor.fetchone()
    print("result = ", resultes)

    # for row in resultes:
    #     print(row[0])
except:
    print("ERROR")
    db.rollback()
# 关闭数据库连接
db.close()