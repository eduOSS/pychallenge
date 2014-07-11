#https://docs.python.org/2/howto/urllib2.html
import urllib2,urllib
from bs4 import BeautifulSoup
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

def read_html(url,value = None):
    req = urllib2.Request(url)
    if value is not None:
        data = urllib.urlencode(value)
        req = url+'?'+ data
    response = urllib2.urlopen(req)
    html = response.read()
    return html 

def main():
    value_nu, value_tag,value = '','',None 
    for i in range(402):
        if i == 0:
            tag_a = BeautifulSoup(read_html(url,None)).a
            href = tag_a['href']
            value_nu = href[-5:]
            value_tag = href[-13:-6]
        else:
            value = {value_tag:value_nu}
            html = read_html(url,value)
            if 'two' in html:
                value_nu=str(int(value_nu)/2)
            elif 'next' in html:
                value_nu = html[-5:]
            else:
                print i, html
                break
    print read_html(url,value)

if __name__ == "__main__":
    main()
