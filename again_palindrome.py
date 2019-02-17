s=input()
f=[]
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        a=s[i:j]
        if a==a[::-1]:
            f.append(a)
c=[]
for i in f:
    c.append(len(i))
#print(f)
f=sorted(f,key=len)
#print(f)
c=sorted(c)
for i in range(len(c)):
    if c[i]!=1:
        print(f[i])
