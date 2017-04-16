'''
Sample Input

2
1 2
3 4
1 2
3 4
Sample Output

[[ 7 10]
 [15 22]]
'''
import numpy

lines_in_matrix = int(raw_input())
a = []
b = []
for _ in range(lines_in_matrix):
    a.append(map(int, raw_input().split(' ')))
for _ in range(lines_in_matrix):
    b.append(map(int, raw_input().split(' ')))
print numpy.dot(a, b)

