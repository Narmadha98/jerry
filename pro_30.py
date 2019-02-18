import sys
from itertools import combinations
def comb(n,k):
    sp=""
    n=list(n)
    p=list(combinations(n,k))
    return p
n=input()
if int(n)%8==0:
    print('yes')
    sys.exit()
else:
    for k in range(len(n)-1,0,-1):
        s=comb(n,k)
        for i in s:
            o=list(i)
            sp=""
            for f in o:
                sp=sp+f
            if(int(sp)%8==0):
                print('yes')
                sys.exit()
print('no')
