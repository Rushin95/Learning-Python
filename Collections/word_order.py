# count the occurences of words

import collections
o = collections.OrderedDict()
n = int(raw_input())
for _ in xrange(n):
    x = raw_input()
    o[x] = o.get(x,0)+1
print len(o)
for key,value in o.items():
    print value,

# Sample Input:
# 4
# bcdef
# abcdefg
# bcde
# bcdef
