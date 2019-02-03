def rightarr(l,k,n):
    for i in range(k):
        rightrotone(l,n)
    print(*l)
def rightrotone(l,n):
    temp=l[n-1]
    for i in range(n-1 ,0,-1):
        l[i]=l[i-1]
    l[0]=temp
n,k=map(int,input().split())
l=list(map(int,input().split()))
s=rightarr(l,k,n)
