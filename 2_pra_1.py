from bs4 import BeautifulSoup, Comment
import urllib2,collections
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
d = collections.defaultdict(int)
for c in comments[1]:
    d[c] += 1
    #print type(d[c]) #all outcomes are int 
#print d[0].__class__ # the result is int
for c in sorted(d, key = d.get,reverse = True):
    print c,d[c]
    #print '$s %d' % (c,int(d[c]))
    #TypeError: %d format: a number is required, not unicode
    # there is no reason!
