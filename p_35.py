s=input()
s1=s.lower()
a=list(s1)
#print(a)
c=[]
r=[]
#a=a.lower()
for i in a:
    x=a.count(i)
    c.append(x)
#print(c)
m=min(c)
#print(m)
for i in range(len(a)):
    if(m==a.count(a[i])):
        r.append(s[i])
sp=""
for i in r:
    sp=sp+i+" "
print(' '.join(sp.split()))
