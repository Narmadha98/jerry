s=int(input())
x=[]
l=list(map(int,input().split()))
for i in range(s):
  c=l.count(l[i])
  d=[c,l[i]]
  x.append(d)
#print(x)
p=min(u[0] for u in x)
for i in x:
  if i[0]==p:
    print(i[1])
  
