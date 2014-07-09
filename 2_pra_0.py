import collections
d = collections.defaultdict(int)
for c in 'a;lfkja;lkfakhfakfahdsfaefnsakjfnhadhfahdfja': 
    d[c] += 1 
print d,'\n'
for c in sorted(d, key = d.get, reverse = True):
    print '%s %6d' % (c,d[c]) 
