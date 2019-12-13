#!/usr/bin/env python
# -*- coding:utf-8 -*-

from jinja2 import Template
template = Template('Hello {{ name }}!')
print(template.render(name='poplarli'))
print(template.render({"name" : "poplar"}))





from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('test'))
template = env.get_template('a.j2');

foo = {"bar": 123};
content = template.render(foo= foo, name='hhh', age='18', country='china')
print(content)
with open("./a.out", 'w') as fp:
    fp.write(content)