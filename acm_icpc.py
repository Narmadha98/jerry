n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
d=[]
for i in range(n):
    if l[i]<5:
        d.append(l[i])
#print(d)
for i in range(len(d)):
    d[i]=d[i]+k
x=[0]*len(d)
for i in range(len(d)):
    if d[i]<=5:
        x[i]=1
    else:
        x[i]=0
m=0
for i in range(len(x)):
    if x[i]==1:
        m=m+1
print(m//3)
