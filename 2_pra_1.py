from bs4 import BeautifulSoup, Comment
import urllib2
url = "http://www.pythonchallenge.com/pc/def/ocr.html"
html = urllib2.urlopen(url).read()
html ='<html><body>'+html+'</html></body>'
#print html
soup = BeautifulSoup(html)

f = lambda text:isinstance(text,Comment)

comments = soup.find_all(text = lambda text:isinstance(text,Comment))
for comment in comments:
    comment.extract()
    print comment
