'''
Sample Input

2 2
1 2
3 4
'''

import numpy
int_matrix= []
for _ in range(int(raw_input().split(' ')[0])):
    integers = list(map(int,raw_input().split(' ')))
    int_matrix.append(integers)
numpy_matrix = numpy.array(int_matrix)
print numpy.mean(numpy_matrix, axis = 1)
print numpy.var(numpy_matrix, axis = 0)
print numpy.std(numpy_matrix, axis = None)