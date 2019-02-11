n,k=map(int,input().split())
l=list(map(int,input().split()))
x=[]
for i in l:
    s=l.count(i)
    if s==k:
        x.append(i)
x=set(x)
d=list(x)
print(*d)
#baaaaaaaaaaaaaaa
        
