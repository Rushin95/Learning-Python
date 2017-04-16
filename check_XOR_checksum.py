# find XOR of the upper n*n matrix
import timeit
def answer():
    start = 17
    len = 4
    a = []
    value = start - 1
    for i in range(len):
        for j in range(0,len - i):
            value += 1
            a.append(value)
        value += i
    print reduce(lambda x, y: x ^ y, a)
print timeit.timeit(answer,number=1)
