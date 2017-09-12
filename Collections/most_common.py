# Find the top 3 common alphabet

from collections import OrderedDict
import sys

if __name__ == "__main__":
    s = raw_input().strip()
    o = OrderedDict()
    for i in s:
        o[i]= o.get(i,0)+1
    o = sorted(o.items(), key=lambda x: (-x[1],x[0]))[0:3]
    for t in o:
        print t[0],t[1]

# Sample Input:
# aabbbccde
