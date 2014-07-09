from bs4 import BeautifulSoup, Comment
html = """
<html>
<head>
<title>alkdfja;l</title>
</head>
<body>
<br>
heloajld
<br>
</body>
</html>

<!--
hello comment 1
-->

<!--
hello comment 2
hhello comment 2hello comment 2hello comment 2hello comment 2ello comment 2
hello comment 2
hello comment 2
hello comment 2
-->

"""
soup = BeautifulSoup(html)

comments = soup.findAll(text = lambda text:isinstance(text,Comment))
print len(comments)
#for comment in comments:
#    comment.extract()
#    print comment
