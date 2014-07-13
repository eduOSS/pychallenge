#references: https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print pairs
pairs = sorted(pairs,key=lambda x: x[0])
print pairs
