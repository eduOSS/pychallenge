#references:http://inteletec.com/python-http-url-request-of-password-protected-remote-server-folder/
#http://www.effbot.org/zone/python-list.htm
#https://gist.github.com/nakamura001/3224974
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


import urllib2,requests,re,StringIO,urllib,glob
from PIL import Image,ImageDraw
from bs4 import BeautifulSoup,Comment

username = 'huge'
password = 'file'
url = 'http://www.pythonchallenge.com/pc/return/good.html'
r = requests.get(url, auth=(username, password))
html = r.content 

soup = BeautifulSoup('<html><body>'+html+'</html></body>')
comment = soup.find_all(text = lambda text: isinstance(text,Comment))[1]
nouse, first, second = comment.replace('second','').replace('-->','').replace('\n','').split(':')
first = [int(i) for i in ''.join(first).split(',')]
second = [int(i) for i in ''.join(second).split(',')]

f = Image.new('RGB',(500,500),'white')
draw = ImageDraw.Draw(f)
draw.line(first,'red',2)
draw.line(second,'red',2)
f.save('bull.png','PNG')
