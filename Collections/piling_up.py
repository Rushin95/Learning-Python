# create a pile of cube in descending order of their lengths
from collections import deque

def check_piling_up(input_list):
    d = deque()
    current_base = max(input_list[0],input_list[-1])
    map(lambda x:d.append(x), input_list)
    while len(d)!= 1:
        left = d.popleft()
        right = d.pop()
        if left>current_base or right>current_base:
            return 'No'
        else:
            if left>=right:
                d.append(right)
                current_base = left
            else:
                d.appendleft(left)
                current_base = right
    last_cube = d.pop()
    if last_cube>current_base:
        return 'No'
    return 'Yes'

def main():
    for _ in xrange(int(raw_input())):
        _ = raw_input()
        print check_piling_up(map(int,raw_input().split()))

if __name__ == '__main__':
    main()

# Sample Input:
# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 2
