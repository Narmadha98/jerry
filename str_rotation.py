def rightarr(l,k,n):
    for i in range(k):
        rightrotone(l,n)
    return l
def rightrotone(l,n):
    temp=l[n-1]
    for i in range(n-1 ,0,-1):
        l[i]=l[i-1]
    l[0]=temp
n1,k=map(str,input().split())
l=list(n1)
sp=""
s=rightarr(l,int(k),len(l))
for i in s:
    sp=sp+i
print(sp.strip())
