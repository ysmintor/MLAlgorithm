#!/usr/bin/python3


with open('/Users/york/Downloads/ConfLongDemo_JSI.txt') as f:
    dict = []
    for line in f.readlines():
        line_arr = line.strip().split(',')
        dict.append(tuple(line_arr))
        # print("read line", tuple(line_arr))

    print("dict", dict)