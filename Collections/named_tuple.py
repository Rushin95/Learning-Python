# find average of the to marks
from collections import namedtuple
n, S = int(raw_input()),namedtuple('S',raw_input())
print "%.2f" % round((sum(float(S(*raw_input().split()).MARKS) for _ in range(n)))/n,2)

# Sample input:
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6
