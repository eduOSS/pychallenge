from bs4 import BeautifulSoup, Comment
import urllib2,urllib
base_url = "http://www.pythonchallenge.com/pc/def/"
source_tail= 'peak.html'
source_url = base_url + source_tail
source_html = urllib2.urlopen(source_url).read()
soup = BeautifulSoup(source_html)
target_tail = soup.peakhell['src']
target_url = base_url + target_tail

target_html = urllib2.urlopen(target_url).read()
output = open('banner.p','wb')
output.write(target_html)
output.close()

import pprint, pickle

pkl_file = open('banner.p', 'rb')

data1 = pickle.load(pkl_file)


for line in data1:
    line_string = ''
    for j in line:
        line_string += j[0]*j[1]
    print line_string

for line in data1:
    print ''.join([j[0]*j[1] for j in line])

#for i in range(len(data1)):
#    pprint.pprint(data1[i])
#print data1
#pprint.pprint(data1)
for line in data1:
    print "".join(map(lambda pair:pair[0]*pair[1],line))
#data2 = pickle.load(pkl_file)
#pprint.pprint(data2)

pkl_file.close()

banner = pickle.loads(target_html)
print '\n'.join( [ "".join( [ i[0]*i[1] for i in b ] ) for b in banner ] )
print '\n'.join(["".join([pair[0]*pair[1] for pair in line]) for line in banner])

print '\n'.join("".join(i[0] * i[1] for i in l) for l in
                __import__('pickle').loads(__import__('urllib').urlopen(
                'http://www.pythonchallenge.com/pc/def/banner.p'
                ).read()))

#bannerurl = "http://www.pythonchallenge.com/pc/def/banner.p"
#url = urllib.urlopen(bannerurl)
#banner = url.read()
#obj = pickle.loads(banner)
#print "\n".join([ reduce(lambda x,y : x + y[0]*y[1], line, "") for line in obj ])

