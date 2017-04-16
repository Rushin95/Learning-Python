def getParent(args):
    rank = (2**args[1])-1
    index = (2**args[1])-1
    if args[0] == index:
        return -1
    while rank > 0:
        left_index = index - (rank + 1)/2
        right_index = index - 1
        if args[0] == left_index or args[0] == right_index:
            return index
        index = left_index if args[0] < left_index else right_index
        rank = (rank -1)/2

def answer(h,q):
    return map(getParent,[(node,h) for node in q])

def main():
    print answer(int(input()),map(int,raw_input().split()))

main()