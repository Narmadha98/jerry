from collections import Counter
a,b=map(str,input().split())
l1=list(a)
l2=list(b)
t=Counter(l1)
x=Counter(l2)
z=list(t.values())
y=list(x.values())
if(z==y):
    print("yes")
else:
    print("no")
