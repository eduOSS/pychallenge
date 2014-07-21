#references:http://stackoverflow.com/questions/553871/can-anyone-provide-a-more-pythonic-way-of-generating-the-morris-sequence
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


from itertools import groupby 

def next_morris(number):
    return ''.join('%s%s' % (len(list(group)), digit) for digit, group in groupby(number))

a = '1'
for i in range(3):
    a = next_morris(a)

print len(a)

