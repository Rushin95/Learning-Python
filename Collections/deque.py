# append and pop fucntion of deque
from collections import deque
d = deque()
for _ in range(int(raw_input())):
    entry = raw_input().split()
    if entry[0] == 'append':
        d.append(entry[1])
    elif entry[0] == 'appendleft':
        d.appendleft(entry[1])
    elif entry[0] == 'pop':
        d.pop()
    elif entry[0] == 'popleft':
        d.popleft()
print ' '.join(str(x) for x in d)

# Sample Input:
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft
