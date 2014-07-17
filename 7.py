#references:
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


import png,urllib2,numpy,itertools,urllib
from PIL import Image
import glob

if not glob.glob('oxygen.png'):
    url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    file = urllib.urlretrieve(url,'oxygen.png')
    print file[0]

im = Image.open('oxygen.png')
x, y = im.size
box = (0,y/2,x,y/2+1)
region = im.crop(box)
region.save('mosaic.png')
im_line = Image.open('mosaic.png')

data_list = list(im_line.getdata())

result = ''.join([chr(data_list[k][0]) for k in range(0,len(data_list),7)])
import re

num_re = re.compile(r'(\d+)')
print ''.join([chr(int(i)) for i in num_re.findall(result)])
