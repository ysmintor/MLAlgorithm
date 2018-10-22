# -*- coding: utf-8 -*-

def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


from functools import reduce
def prod(L):
    pass

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))