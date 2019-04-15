#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 中国天气网站爬取天气信息并存储在数据库中
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from bs4 import BeautifulSoup
import requests
import pymysql

conn = pymysql.connect(host='localhost', user='web2_yorkyu_com', passwd = 'bcG6wyk2yW',
db = 'web2_yorkyu_com', port = 3306,charset = 'utf8')

cursor = conn.cursor()
sql = "TRUNCATE TABLE weathers"
try:
    cursor.execute(sql)
    conn.commit()
except:
    print("Error: unable to delete")
    conn.commit()


def get_temperature(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 63.0.323.132Safari / 537.36'} # 设置头文件信息
    response = requests.get(url, headers=headers).content  # 提交requests   get 请求
    soup = BeautifulSoup(response, "html.parser")  # 用Beautifulsoup进行解析
    conmid = soup.find('div', class_='conMidtab')
    conmid2 = conmid.findAll('div', class_='conMidtab2')
    for info in conmid2:
        tr_list = info.find_all('tr')[2:]  # 使用切片取到第三个 tr 标签
        for index, tr in enumerate(tr_list):  # enumerate 可以返回元素的位置及内容
            td_list = tr.find_all('td')
            if index == 0:
                province_name = td_list[0].text.replace('\n', '')
                # 取每个标签的 text 信息，并使用 replace()函数将换行符删除
                city_name = td_list[1].text.replace('\n', '')
                weather = td_list[5].text.replace('\n', '')
                wind = td_list[6].text.replace('\n', '')
                max = td_list[4].text.replace('\n', '')
                min = td_list[7].text.replace('\n', '')
                print(province_name)
            else:
                city_name = td_list[0].text.replace('\n', '')
                weather = td_list[4].text.replace('\n', '')
                wind = td_list[5].text.replace('\n', '')
                max = td_list[3].text.replace('\n', '')
                min = td_list[6].text.replace('\n', '')
                cursor.execute('insert into weathers(city, weather, wind, max, min) values( % s, % s, % s, % s, % s)', (city_name, weather, wind, max, min))

if __name__ == '__main__':
    urls = ['http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml']
    for url in urls:
        get_temperature(url)
    conn.commit()
