n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
co=0
l=sorted(l,reverse=True)
for i in range(n):
    while(c<k):
        c=c+l[i]
        co=co+1
    if c>k:
        c=c-l[i]
        co=co-1
print(co)
