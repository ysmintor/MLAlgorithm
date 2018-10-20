# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print('hello', name)


s = set(L)
s.add('Lisaa')
print(s)


d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

tuple = (1, 2, 3)
tuple2 = (1, [2, 3])
print(d)

s.add(tuple2)       #TypeError: unhashable type: 'list'
s.add(tuple)
print('set = ', s)