# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    print('not_ devisible', n)
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印 1000 以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


"""
@Date    : 2017/11/24 0024
@Author  : TaoYuan (1876665310@qq.com)
@Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
@Version : V1.0.0
@des     : 判断是否为回数
"""


def is_palindrome(n):
    return str(n) == str(n)[::-1]


output = filter(is_palindrome, range(1, 1000))
print(list(output))
