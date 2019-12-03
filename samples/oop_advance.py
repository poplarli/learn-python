#!/usr/bin/env python
# -*- coding:utf-8 -*-

from types import MethodType

class Student(object):
    # Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
    #__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    #除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
    __slots__ = ('name', 'age', 'set_age');

s = Student()
#给实例绑定一个属性
s.name = 'Bh'

#给实例绑定一个方法
#给一个实例绑定的方法，对另一个实例是不起作用的
def set_age(self, age):
    self.age = age;

s.set_age = MethodType(set_age, s)
s.set_age(10)
print(s.age)

#给class绑定方法后，所有实例均可调用
Student.set_age = set_age

#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查
#把一个getter方法变成属性，只需要加上@property就可以了
class Cat(object):
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, v):
        self.__age = v

c =Cat();
c.age = 10;
print(c.age)

#在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系






#解读错误信息是定位错误的关键。我们从上往下可以看到整个错误的调用函数链
#Python内置的logging模块可以非常容易地记录错误信息
import  logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except ZeroDivisionError as e:
        logging.exception(e)
    finally:
        print('END')

main()
print('hehe')