#!/usr/bin/env python
# -*- coding:utf-8 -*-

#object表示该类是从哪个类继承下来的.通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
    #__init__方法的第一个参数永远是self，表示创建的实例本身
    def __init__(self, name, score):
        self.__name = name;
        self.__score = score;
    #和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
    def print_socre(self):
        print('%s, %s' % (self.__name, self.__score))
    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score > 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name

bart = Student('ly', 100)
bart.print_socre()
print(bart.get_grade())
print(bart)

#和静态语言不同，Python允许对实例变量绑定任何数据
bart.age = 20
#虽然不能直接访问__name，但是python解释器对外把__name变量改成了_Student__name，所以可以则有访问。但是不要这么干哦
#Python本身没有任何机制阻止你干坏事，一切全靠自觉。
bart._Student__name
#这个只是新增了一个__name变量哦
bart.__name='yl'
print(bart.get_name())

#动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

class Animal(object):
    def run(self):
        print('animal is running')

class Dog(Animal):
    cnt = 0
    name = 'DOG'
    def __init__(self):
        Dog.cnt = Dog.cnt + 1
    def run(self):
        print('dog is running')
    def __len__(self):
        return 100;

def runtwice(animal):
    animal.run()
    animal.run()

runtwice(Animal())
runtwice(Dog())

#type()函数返回的是什么类型呢？它返回对应的Class类型
print(type(123))
print(type(Animal()))

#能用type()判断的基本类型也可以用isinstance()判断。总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”
print(isinstance(Dog(), Animal))

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
print(dir(Animal))
print(dir(Student))



dg = Dog()
print(hasattr(dg, 'run2'))
print(len(dg))
fn = getattr(dg, 'run')
fn()

#name是Dog的类属性
#不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
print(dg.name)
dg.name = 'Hasky'
print(dg.name)
del dg.name
print(dg.name)

print(dg.cnt)