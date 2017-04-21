def show_lcm(a,b):
    if a>b:
        highest = a
    else:
        highest = b
    while True:
        if highest%a==0 and highest%b==0 :
            answer = highest
            break
        highest += 1
    return answer

print 'LCM is', show_lcm(54,24)
