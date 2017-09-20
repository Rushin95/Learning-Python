# Sort them in ascending order then print them in the standard format

def wrapper(f):
    extension = '+91'
    def fun(l):
        # complete the function
        print '\n'.join(map(lambda x: ' '.join([extension,x[-10:-5],x[-5:]]),sorted(map(lambda x: x[-10:],l))))
    return fun

@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l)


# Sample Input:
# 3
# 07895462130
# 919875641230
# 9195969878
