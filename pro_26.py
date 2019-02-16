n=int(input())
l=list(map(int,input().split()))
c=[]
co=1
for i in l:
  if i not in c:
    c.append(i)
for i in range(0,len(c)-1):
  if c[i]<c[i+1]:
    co=co+1
print(c)
