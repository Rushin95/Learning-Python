import numpy
matrix = []
for i in range(int(raw_input())):
    matrix.append(map(float, raw_input().split(' ')))
print numpy.linalg.det(matrix)

'''
Sample Input

2
1.1 1.1
1.1 1.1
Sample Output

0.0
'''