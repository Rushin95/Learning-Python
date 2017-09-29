# Evaluate string like a mathematical equation
#!/bin/python

import sys
import operator

def solve(opr):
    # Complete this function
    op = {'+': operator.add, '-':operator.sub}
    digit1 = int(opr[0])
    function = opr[1]
    digit2 = int(opr[2])
    return op[function](digit1,digit2)

if __name__ == "__main__":
    opr = raw_input().strip()
    result = solve(opr)
    print result

# Sample input:
# '1+3'
