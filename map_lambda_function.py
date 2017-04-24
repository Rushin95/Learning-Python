cube = lambda x:x**3 # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    flist = [0, 1]
    for i in range(2, n):
        flist.append(flist[i-1] + flist[i-2])
    return flist

if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))

'''
Sample Input

5
Sample Output

[0, 1, 1, 8, 27]
'''