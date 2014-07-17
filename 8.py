#references:http://stackoverflow.com/questions/7784148/understanding-repr-function-in-python/7784214#7784214
#http://effbot.org/librarybook/bz2.htm
#here is a useful one: http://pymotw.com/2/bz2/index.html
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']

import urllib2,re,bz2
un,pw =[bz2.decompress(eval(i)) for i in re.findall(r'(\'.+\')',urllib2.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').read())]
print un,pw
