#references:
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


import zipfile, re
findnothing = re.compile(r"Next nothing is (\d+)").match
comments = []
z = zipfile.ZipFile("channel.zip", "r")
seed = "90052"
while True:
    fname = seed + ".txt"
    comments.append(z.getinfo(fname).comment)
    guts = z.read(fname)
    m = findnothing(guts)
    if m:
        seed = m.group(1)
    else:
        break
print "".join(comments)
