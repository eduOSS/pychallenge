#references:http://stackoverflow.com/questions/7784148/understanding-repr-function-in-python/7784214#7784214
#http://effbot.org/librarybook/bz2.htm
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']

import urllib2,re,bz2
url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
html = urllib2.urlopen(url).read()
un,pw =[bz2.decompress(eval(i)) for i in re.findall(r'(\'.+\')',html)]
#l = "the meaning of life" 
#l1 = bz2.compress(l)
#l2 = bz2.decompress(l1)
#print repr(l1),'\n',l2
print un,pw
#print repr(un),repr(pw)
un, pw = re.findall(r'(\'.+\')',html)
print type(eval(un)),'**',type(pw)
print eval(un).decode('bz2'),eval(pw).decode('bz2')
#print '*********'
#print eval("BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08").encode('bz2')
