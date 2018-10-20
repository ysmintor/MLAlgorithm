def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(5))

for n in fib(6):
    print(n)
g = fib(6)
while True:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def triangles():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]

d = triangles()
for i in range(100):
    print(next(d))