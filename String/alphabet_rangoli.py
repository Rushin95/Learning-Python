def print_rangoli(size):
    # your code goes here
    if size == 1:
        print 'a'
    else:
        l= ''
        ans = []
        ans_str =''
        for i in range(size,0,-1):
            alpha = chr(96+i)
            s = '-'.join(l+alpha+l[::-1])
            s = s.center(1+2*(size-1)+2*(size-1), '-')
            print s
            ans.append(s)
            l+= alpha
        for each in ans[size-2::-1]:
            print each

print_rangoli(4)
