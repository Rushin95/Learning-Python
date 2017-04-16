import numpy
coefficients = map(float,raw_input().split(' '))
x_value = int(raw_input())
value_of_poly = numpy.polyval(coefficients, x_value)
print value_of_poly

'''
Sample Input

1.1 2 3
0
Sample Output

3.0
'''