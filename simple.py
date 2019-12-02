#!/usr/bin/env python
# -*- coding:utf-8 -*-

print("123");
print('''
hahah
llll
aaa
''')

print(1>0);

classmates=['xiaoming','xiaowang', 123];
print(classmates[0])
print(classmates[-1])
classmates.pop(1)
print(classmates[1])

teachers=('dazhang', 'daniu');
print(teachers)

t=(1,)
print(t[0])


#age = input("enter a number:")
#age=int(age)
age=12
if age >= 18:
    print("adult")
elif age >= 8:
    print("child")
else:
    print("baby")

for name in teachers:
    print(name)

for x in range(5):
    print(x)

print(list(range(10)))

n = 0
sum = 0
while n < 10:
    sum += n
    n = n + 2
print("sum=", sum)

#dict的key是不可变对象，所以不能为list
d={"a":1, "b":2}
print(d["a"])
print(d.get('c', -1))

#set的同样必须放入不可变对象
#无序 不重复
s=set([1,2,3,4,1,2])
s.add('haha')
s.add((10,11))
print(s)

#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。



print("abs(-1) = ",abs(-1))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type");
    if x>=0:
        return x;
    else:
        return -x;

print("my_abs(-1) = ", my_abs(-1));

def func():
    #占位符
    pass

#看起来func2返回了两个值，其实返回的是个tuple
def func2(x, y):
    return x+1, y+1

a,b = func2(1,2)
print(func2(1,2), a, b);


#默认参数必须指向不变对象！要不然可能会随着函数的调用不断变化，会很奇怪哦,如下。
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())


def add_end2(L = None):
    if(L == None):
        L = []
    L.append('END')
    return L;
print(add_end2())
print(add_end2())


def pow(x, y = 2):
    res = 1;
    n = y;
    while n > 0:
        res = res * x;
        n = n - 1;
    return res;

print("pow(2, 4) = ", pow(2, 4))
print("pow(2) = ", pow(2))

#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
def cal(*nums):
    sum = 0;
    for x in nums:
        sum = sum + x;
    return sum;
print("cal(1,2,10) = ", cal(1,2,10))

#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums=[1,2,3]
print("cal(*nums) = ", cal(*nums))

#关键字参数
def person(name, age, **kw):
    print(name, age, kw)
person('pp', 31)
person('pp', 31, city='shanghai', job='farmer')
#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'beijing', 'job': 'worker'}
person('qq', 20, **extra)

#命名关键字参数
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person2(name, age, *, city, job):
    print(name, age, city, job)
person2('tt', 30, city = 'guangzhou', job = 'none')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)
person3('tt', 30, city = 'guangzhou', job = 'none222')

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
#虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。

def fact(x):
    if x==1:
        return 1;
    return x * fact(x - 1);
print("fact(5) = ", fact(5))