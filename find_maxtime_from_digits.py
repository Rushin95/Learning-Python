import itertools
input_strng = list(map(int, raw_input().split(' ')))
l =  list(itertools.permutations(input_strng))
pool = list()
for i in l:
    s = map(str, i)
    s.append('')
    newstrng = str(''.join(s))
    if int(newstrng[:2]) < 24 and int(newstrng[2:]) < 60:
        pool.append(i)
if(len(pool)== 0):
    print 'NOT POSSIBLE'
else:
    maxtime = str(''.join(map(str, max(pool))))
    print maxtime[:2]+':' + maxtime[2:]
