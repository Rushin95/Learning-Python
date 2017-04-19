def square(num):
    for i in xrange(1, num+1):
        yield i*i

# One-line generator
# square_of_nums = (x*x for x in xrange(num))

def main():
    square_of_nums = square(10)
    for s in square_of_nums:
        print s


main()