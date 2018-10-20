def calc(*numbers):
    sum = 0
    for n in numbers:
        sum +=  n**2;
    return sum

print(calc(*[1, 2]))

# hanoi
def mov(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        mov(n-1, a, c, b)
        print(a, '-->', c)
        mov(n-1, b, a, c)

mov(3, 'A', 'B', 'C')