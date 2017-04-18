def fib(n):
    a,b,counter = 0,1,0
    while True:
        if counter>n: return
        yield a
        a,b = b,a+b
        counter+=1

def main():
    f5 = fib(5)
    for i in f5:
        print i

main()



