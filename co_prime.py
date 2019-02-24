def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
s1,s2=map(str,input().split())
x=len(s1)
y=len(s2)
Z=gcd(x,y)
if Z==1:
    print('yes')
else:
    print('no')
