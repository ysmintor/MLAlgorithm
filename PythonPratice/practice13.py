import functools
max2 = functools.partial(max, 10)
maxitem = max2(5, 6, 7)
print('max item  =', maxitem)
