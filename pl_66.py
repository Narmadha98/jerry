n=list(map(int,input().split()))
l=list(map(int,input().split()))
x=[]
k=n[len(n)-1]
for i in l:
    s=l.count(i)
    if s==k:
        x.append(i)
x=set(x)
d=list(x)
print(*d)
#baaaaaaaaaaaaaaa
        
