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
p=max(c)
for i in f:
    if p==len(i):
        print(i)
        break
