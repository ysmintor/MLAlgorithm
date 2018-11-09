type(123)
print(type(123))

print(dir('ABC'))

class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)

s2 = Student()
s2.set_age(25)
