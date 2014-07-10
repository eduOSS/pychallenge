from string import letters
from bs4 import BeautifulSoup, Comment
import urllib2,collections,string,re
url = "http://www.pythonchallenge.com/pc/def/ocr.html"
html = urllib2.urlopen(url).read()
html ='<html><body>'+html+'</html></body>'
#print html
soup = BeautifulSoup(html)

f = lambda text:isinstance(text,Comment)

comments = soup.find_all(text = lambda text:isinstance(text,Comment))
#for comment in comments:
#    comment.extract()
#    print comment
#d = collections.defaultdict(int)
#for c in comments[1]:
#    d[c] += 1
#    #print d[c]
#print d[0].__class__
#for c in sorted(d, key = d.get,reverse = True):
#    #print c,d[c]
#    print '%s %d' % (c,d[c])
#typeError: %d format: a number is required, not unicode 
text = comments[1]
#print filter(lambda x: x in string.letters, text)
#print re.findall(r'[a-z]',text)
#print ''.join([x for x in text if x in letters])
#textlist = set(text)
#for i in textlist:
#    print i, text.count(i)
for ch in text:
    if ch.isalpha():
        print ch
