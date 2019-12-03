#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import Iterable
from collections import Iterator
import os
from functools import reduce

L=['mc', 'sa', 'ty'];
print(L[0:2])

L=list(range(100))
print(L[::10])
print(L[-10:])

d={'a': 1, 'b':2,'c':3}
for k in d:
    print("k=", k)
for value in d.values():
    print("v=", value)
for k, v in d.items():
    print("k=", k, "v=", v)

#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
#可以通过collections模块的Iterable类型判断
print(isinstance('abc', Iterable))
print(isinstance(100, Iterable))

for i, v in enumerate([1,2,3]):
    print(i, v)

for x, y in [(1,1),(2,2),(3,3)]:
    print(x, y)


#运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
L=[m+n for m in 'ABC' for n in 'abc']
print (L)
L=[x*x for x in range(1,11) if x % 2 == 0]
print (L)

L=[d for d in os.listdir('.')]
print (L)

L=[k + '=' + str(v) for k, v in d.items()]
print(L)

L=['Hello', 'wORLD', 18, 'hI']
print([s.lower() for s in L if isinstance(s, str)])


#生成器 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
g = (i for i in range(10))
print(g)
#print(next(g))
#print(next(g))
#我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误
for n in g:
    #print(n)
    pass

#fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(5)

#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
#请注意区分普通函数和generator函数，普通函数调用直接返回结果; generator函数的“调用”实际返回一个generator对象：
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n +1
    return 'done'

f = fib2(5)
for x in f:
    print(x)

try:
    next(f)
except StopIteration as e:
    print(e.value)

#可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#包括集合数据类型和generator
print(isinstance(f, Iterable))


#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print(isinstance((x for x in range(5)), Iterator))

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))

#Python的for循环本质上就是通过不断调用next()函数实现的
it = iter(list(range(10)))
while True:
    try:
        print(next(it))
    except StopIteration:
        break;



#变量可以指向函数
f = abs;
print(f)
print(f(-10))

#函数名也是变量
#实际代码绝对不能这么写，这里是为了说明函数名也是变量
#abs = 10

#传入函数
#函数的参数能够接收别的函数。
def add(x, y, f):
    return f(x) + f(y)

print(add(-3, 5, abs))


#map/reduce
def f(x):
    return x * x
#map函数接受两个参数，第一个为函数，第二个为Iterable
r= map(f, [1,3,5,7,9])
#r是一个Iterator，一个堕性序列，通过list函数将整个序列计算出来并返回一个list
print(isinstance(r, Iterator))
print(list(r))
print(list(map(str, [1,2,3,4,5])))


def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1,3,5,7,9]))

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, '13579')))

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y;
    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num, s))


#用filter()这个高阶函数，关键在于正确实现一个“筛选”函数
#filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, list(range(20)))))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 10:
        print(n)
    else:
        break


#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted([-1,2,-9,10,8]))
print(sorted([-1,2,-9,10,8], key=abs))
#忽略大小写，反向排序
print(sorted(['Alice', 'celia', 'Bruce'], key = str.lower, reverse=True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按名字排序
print(sorted(L, key=lambda x : x[0]))
#按分数排序
print(sorted(L, key=lambda x : x[1]))

#函数可以作为返回值
#lazy_sum中定义了sum，内部sum可以引用外部函数的参数和局部变量，当lazy_sum返回函数sum时，相关的参数和变量都保存在返回的函数中，称为闭包
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def lazy_sum(*args):
    def sum():
        ax = 0;
        for n in args:
            ax = n + ax
            n = n + 1
        return ax
    return sum;

print(lazy_sum(1,2,3,4,5))
print(lazy_sum(1,2,3,4,5)())

#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突
print(list(map(lambda x : x + 1, [1,2,3])))
#匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x : x * x
print(f(10))
#也可以将匿名函数作为返回值返回
def build(x, y):
    return lambda : x*x + y*y

print(build(2,3)())

L=list(filter(lambda x : x % 3 == 0, list(range(30))))
print(L)

#函数对象有一个__name__属性，可以拿到函数的名字
print(build.__name__)


#偏函数
import functools
#functools.partial的作用就是，把一个函数的某些参数给固定住
int2 = functools.partial(int, base=2)
print(int2('100'))
#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数



