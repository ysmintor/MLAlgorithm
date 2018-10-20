# -*- coding: utf-8 -*-
import math
def quadratic(a, b, c):
    delta_sqrt = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + delta_sqrt) / 2*a
    x2 = (-b - delta_sqrt) / 2*a
    return x1, x2



print(quadratic(2, 3, 1))# => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)
