import math
def perfsq(i):
    fl=0
    a=math.sqrt(i)
    b=math.floor(a)
    if(i==b*b):
        fl=1
    else:
        fl=0
    return fl
a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    s=perfsq(i)
    if(s==1):
        c+=1
print(c)
