from collections import Counter
s1,s2,k=map(str,input().split())
k=int(k)
t=Counter(s1)-Counter(s2)
x=t.values()
x=list(x)
if(sum(x)==k):
    print('yes')
else:
    print('no')
