def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
n,q=map(int,input().split())
a=list(map(int,input().split()))
w=[]
while q!=0:
    x,y=map(int,input().split())
    z=gcd(a[x-1],a[y-1])
    w.append(z)
    q=q-1
for i in w:
    print(i)
