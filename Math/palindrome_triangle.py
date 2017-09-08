print "\n".join(["".join(map(str, range(1,x+1)+range(x-1,0,-1))) for x in range(1,int(raw_input())+1)])
