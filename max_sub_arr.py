def mul(l):
    max_a=-sys.maxsize-1
    max_until=1
    for i in range(len(l)):
        max_until=max_until*l[i]
        if max_until==0:
            max_until=0
            continue
        if max_a<max_until:
            max_a=max_until
    return max_a
import sys
n=int(input())
l=list(map(int,input().split()))
a=mul(l)
l=l[::-1]
b=mul(l)
print(max(a,b))
