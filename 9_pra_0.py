#references:http://inteletec.com/python-http-url-request-of-password-protected-remote-server-folder/
#https://gist.github.com/nakamura001/3224974
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


import urllib2,requests,re,StringIO,urllib,glob
from PIL import Image,ImageDraw
from bs4 import BeautifulSoup,Comment
from StringIO import StringIO
username = 'huge'
password = 'file'
url = 'http://www.pythonchallenge.com/pc/return/good.html'
img_url = 'http://www.pythonchallenge.com/pc/return/good.jpg'
r = requests.get(url, auth=(username, password))
#html = urllib2.urlopen(url).read()
html = r.content 
soup = BeautifulSoup('<html><body>'+html+'</html></body>')
comment = soup.find_all(text = lambda text: isinstance(text,Comment))[1]
#num_list = re.split(':|,',comment.replace('\n','').replace('second:',','))[1:]
#num = re.findall(r'first:(\d+)\n\n',html)
#print len(num_list)
nouse, first, second = comment.replace('second','').replace('-->','').replace('\n','').split(':')
#print first,'\n\n', second
first = [int(i) for i in ''.join(first).split(',')]
second = [int(i) for i in ''.join(second).split(',')]
#coords = zip(first,second)

name = 'base.jpg'
if not glob.glob(name):
    r_img = requests.get(img_url, auth=(username, password))
    #im = Image.open(StringIO(r_img.content))
    f = open(name,'wb')
    f.write(r_img.content)
    f.close()


#Image.open(name).save('base.png')
#f = Image.open('base.png')
f = Image.new('RGB',(500,500),'white')
draw = ImageDraw.Draw(f)
draw.line(first,'red',2)
draw.line(second,'red',2)
#draw.polygon(coords,outline = 'black')
#draw.line(coords,width = 5)
i = iter(first)
for k in range(len(first)/2):
    #p=getPixel(f,coords[i][0],coords[i][1])
    #p=f.getPixel(coords[i][0],coords[i][1])
    draw.point((i.next(),i.next()),fill = 'black')

j = iter(second)
for k in range(len(second)/2):
    #p=getPixel(f,coords[i][0],coords[i][1])
    #p=f.getPixel(coords[i][0],coords[i][1])
    draw.point((j.next(),j.next()),fill = 'black')
f.save('base1.png')
f.close()
#f.save('file.png')    
#im.save(name,'JPEG')
#print im.getdata()
#print comment
#im = requests.get(jpg_url,auth=(username,password))
#print im
#value = {
#        'username': username,
#        'password': password
#        }
#data = urllib.urlencode(value)
#req = urllib2.Request(jpg_url,data)
#response = urllib2.urlopen(req)
#im = StringIO.StringIO(response.read())
#print im.info
