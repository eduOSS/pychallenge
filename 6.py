import urllib2,zipfile,re,urllib,os,datetime,requests

zip_url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
zip_name = zip_url.split('/')[-1]

if not os.path.exists('channel.zip'):
    zip_file = urllib.urlretrieve(zip_url,zip_name)
#    zip_file = requests.get(zip_url)
    print 'download file'

try:
    zf = zipfile.ZipFile(zip_name,'r')
except Exception as e:
    print e[0],type(e)

#comments = '' 
##for info in zf.infolist():
#for info in zf.infolist():
#    comment = info.comment   
#    if comment:
#        comments += comment
#print ''.join(comments)
#for chr in set(comments):
#    print chr,'  ',comments.count(chr)
#made it the six one! 

#readme = zf.read('readme.txt')
#print readme

comments = []
file_name = '90052.txt'
file_string = ''
i = 2  
while file_name:
    #print file_name
    file_string = zf.read(file_name)
    for s in file_string.split():
        if s.isdigit():
            i += 1
            file_name = s+'.txt'
            comments.append(zf.getinfo(file_name).comment)
#            size = zf.getinfo(file_name).file_size 
#            if  size > 21:
#                print file_name,size
        else:
            file_name = False

print file_string,i
print ''.join(comments)

#print zf.read('46145.txt')

