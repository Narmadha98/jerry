input()
a=list(map(str,input().split()))
b=list(map(str,input().split()))
c=[]
for i in a:
  if i in b:
    c.append(i)
x=set(c)
d=list(x)
d=sorted(d)
print(*d)
