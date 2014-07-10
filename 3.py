from string import letters
from bs4 import BeautifulSoup, Comment
import urllib2,collections,string,re
url = "http://www.pythonchallenge.com/pc/def/equality.html"
html = urllib2.urlopen(url).read()
#html ='<html><body>'+html+'</html></body>'
#print html
soup = BeautifulSoup(html)

f = lambda text:isinstance(text,Comment)

comments = soup.find_all(text = lambda text:isinstance(text,Comment))
text = comments[0].replace('\n','')
#print len(set(text))
#print set(text)
#print comments,text
#for i in range(4,len(text)-4):
#    if text[i].islower and text[i-4].islower and text[i+4].islower:
#        for j in range(1,4):
#            if text[i-j].isupper and text[i+j].isupper:
#                print text[i-4:i+4]
fre = re.compile(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')
list = fre.findall(text)
cha = ''
for i in list:
    cha += i[len(i)/2]
print cha
#fre = re.compile(r'BODYGUARD{3}[a-z]BODYGUARD{3}')
#fre = re.compile(r'[a-z][A-Z][a-z][A-Z][a-z][A-Z]{3}[a-z]') 
#fre = re.compile(r'[A-Z]{3,}[a-z][A-Z]{3,}')
#print fre.findall(text)
