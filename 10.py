#references:
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


from itertools import groupby 

def next_morris(number):
    return ''.join('%s%s' % (len(list(group)), digit)
                   for digit, group in groupby(number))

a = '1'
for i in range(30):
    a = next_morris(a)

print len(a)
