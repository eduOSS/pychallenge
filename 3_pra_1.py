from string import letters
from bs4 import BeautifulSoup, Comment
import urllib2,collections,string,re
url = "http://www.pythonchallenge.com/pc/def/equality.html"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

f = lambda text:isinstance(text,Comment)

comments = soup.find_all(text = lambda text:isinstance(text,Comment))
text = comments[0].replace('\n','')

markers = ''.join( [ '0' if c in string.lowercase else '1' for c in text] )
def f( res, text, markers ):
    n = len(markers.partition('011101110')[0])
    return f( res+text[n+4], text[n+9:], markers[n+9:] ) if n != len(markers) else res
print f( '', text, markers )

word = ''
for i in range(len(text) - 8):
    if [c for c in text[i:i+9] if c in string.lowercase] == [text[i], text[i+4], text[i+8]]:
        word += text[i+4]
print word
