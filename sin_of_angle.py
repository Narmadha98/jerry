import math
n=int(input())
x=n*(math.pi/180)
#print(x)
if x<1 and x > 0:
    print(round(math.sin(x),1))
else:
    print(round(math.sin(x)))
