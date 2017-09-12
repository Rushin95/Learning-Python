# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
o,n = OrderedDict(), int(raw_input())
for _ in xrange(n):
    entry = raw_input().split()
    net_price = entry[-1]
    item_name = ' '.join(entry[:-1])
    o[item_name] = o.get(item_name,0)+int(net_price)

for key,value in o.items():
    print key,value

# Sample Input:
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
