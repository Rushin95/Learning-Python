def answer(l):
    n = len(l)
    new_list = []
    l.sort()
    print 'l', l
    for i in range(0,n):
        for j in range(i + 1,n):
            if l[j] % l[i] == 0:
                for k in range(j + 1,n):
                    if l[k] % l[j] == 0:
                        new_list.append([l[i],l[j],l[k]])
    return len(new_list)

print answer([1,2,3,4,5,6])
