import math
a,b=map(int,input().split())
c=a*b
a=math.sqrt(c)
b=math.floor(a)
if(a==b):
    print("yes")
else:
    print("no")
