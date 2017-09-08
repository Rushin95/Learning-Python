# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
a,b = map(int,raw_input().split())

d = defaultdict(list)
for i in range(a):
    d['a'].append(raw_input())
for _ in range(b):
    d['b'].append(raw_input())

for m in d['b']:
    ans = []
    for idxn,n in enumerate(d['a']):
        if m == n :
            ans.append(str(idxn+1))           
    if len(ans)!= 0:
        print ' '.join(ans)
    else:
        print -1

# Sample input:
# 5 2
# a
# a
# b
# a
# b
# a
# b
