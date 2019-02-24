n=int(input())
l=list(map(int,input().split()))
s=l.count(0)
m=[]
for i in range(n):
    if l[i]!=0:
        m.append(l[i])
#print(m)
for i in range(s):
    m.append(0)
print(*m)
