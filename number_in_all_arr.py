n,k=map(int,input().split())
l=[]
c=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(k):
    if all(l[0][i] in l[j] for j in range(1,n)):
        c=c+[l[0][i]]
c=sorted(c)
print(*c)
