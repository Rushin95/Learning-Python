def print_formatted(number):
    # your code goes here
    l = len("{0:b}".format(number))
    for num in range(1,number+1):
        print str(num).rjust(l),str(int(oct(num))).rjust(l),"{0:x}".format(num).upper().rjust(l),"{0:b}".format(num).rjust(l)

def main():
    n = int(raw_input())
    print_formatted(n)
