n=int(input())
l=list(map(int,input().split()))
s=0
j=[]
for i in range(n):
    s=s+l[i]
    j.append(s)
print(*j)
