#!/usr/bin/env python
# -*- coding:utf-8 -*-

#在Python中，一个.py文件就称之为一个模块（Module）
#我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。
#可以通过包来组织模块，避免冲突。方法是选择一个顶层包名.
#每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码
# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

'my module'

import sys

def f():
    n = len(sys.argv)
    if n <= 1:
        print('hello python')
    else:
        print('hi python')

if __name__ == '__main__':
    f();
