s=input()
f=[]  
for i in range(len(s)+1):
    for j in range(len(s)+1):
        a=s[i:j]
        if(a==a[::-1]):
            f.append(a)
c=[]
#print(f)
for i in f:
    c.append(len(i))
p=max(c)
#print(c)
print(len(s)-p)
