import numpy
matrix_1 = map(int,raw_input().split(' '))
matrix_2 = map(int,raw_input().split(' '))
print numpy.inner(matrix_1, matrix_2)
print numpy.outer(matrix_1, matrix_2)
'''
Sample Input

0 1
2 3
Sample Output

3
[[0 0]
 [2 3]]
'''
