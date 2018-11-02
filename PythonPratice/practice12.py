

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 相当于 now = log(now)
@log
def now():
    print('2015-3-25')


f = now
f()
import time,functools
# 装饰器
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start=time.time()
        fn(*args,**kw)
        end=time.time()
        print('%s execute in %s ms' %(fn.__name__,end-start))
        return fn(*args,**kw)
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

f=fast(11,22)
print(f)

