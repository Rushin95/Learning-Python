def answer(xs):
    pos_num = []
    neg_num = []
    for i in xs:
        pos_num.append(i) if i >= 0 else neg_num.append(i) if i < 0 else None
    if len(neg_num) != 0 and len(neg_num) % 2 != 0:
        neg_num.remove(max(neg_num))
        if 0 in pos_num:
            while 0 in pos_num:
                    pos_num.remove(0)
    else:
        if 0 in pos_num:
            while 0 in pos_num:
                    pos_num.remove(0)
        else:
            pos_num.remove(min(pos_num))
    if len(pos_num+neg_num)!=0:
        print str(reduce((lambda x, y: x*y), neg_num+pos_num))
    else:
        print str(reduce((lambda x, y: x*y),xs))
answer([-1])