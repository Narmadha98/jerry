s=input()
s1=s.lower()
s1=s1.replace(" ","")
a=list(s1)
c=[]
r=[]
#a=a.lower()
for i in range(len(a)):
    x=a.count(a[i])
    c.append(x)
m=min(c)
for i in s:
    if(m==a.count(i)):
        r.append(i)
print(*r)
