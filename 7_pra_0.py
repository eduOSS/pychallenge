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
#cannot download pic file from url using urlopen
#if not glob.glob('oxygen.png'):
#    url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
#    file = urllib.urlopen(url,'oxygen.png').read()
#    print file[0]
im = Image.open('oxygen.png')
#print im.info
#image_2d = numpy.vstack(itertools.imap(numpy.uint16, pngdata.read()))
#print image_2d
x, y = im.size
box = (0,y/2,x,y/2+1)
region = im.crop(box)
region.save('mosaic.png')
im_line = Image.open('mosaic.png')

data_list = list(im_line.getdata())
#for k in range(0,len(data_list),7):
#    print chr(data_list[k][0])

result = ''.join([chr(data_list[k][0]) for k in range(0,len(data_list),7)])
import re
#num_list = re.findall('.+(\[.+\].+)',result)
#for i in result.replace('[',',').replace(']',',').replace('\'',',').replace(' ','').split(',')print i
print ''.join([chr(int(i)) for i in result.replace('[',',').replace(']',',').replace("'",',').replace(' ','').split(',') if i.isdigit()])

num_re = re.compile(r'(\d+)')
print ''.join([chr(int(i)) for i in num_re.findall(result)])
#print num_list

#box1 = (7,y/2-7,x,y/2+7)
#region1 = im.crop(box1)
#region1.save('mosaic1.png')
#print source,im.info
from PIL import ImageFilter
#im = Image.open('mosaic.png')
#r,g,b,a = im.split()
#print r
#print g
#print b
#print a
#out = im.filter(ImageFilter.DETAIL)
##print out,im.info
#data = im.tostring("raw","RGBA")
#for p in data:
#    print p,'ord: ',ord(p)


