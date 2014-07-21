#references:
#https://en.wikipedia.org/wiki/Look-and-say_sequence
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


a = '1'
b = ''
for i in range(30):
    j = 0
    while j < len(a):
        st = 0
        while j+st < len(a) and a[j] is a[j+st]:
            st += 1
        b = b + str(st) + a[j]
        j = j + st 
    #if len(a) > 1 and a[-2] is not '1':
    #    b += '11'
    a = b
    b = ''
print len(a)


