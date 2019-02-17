s=input()
o=[]
d=['a','e','i','o','u']
s=list(s)
f=[]
for i in range(len(s)):
    if s[i] in d:
        o.append(s[i])
        f.append(i)
e=[]
for i in range(len(s)):
    if i not in f:
        e.append(s[i])
sp=""
for i in o:
    sp=sp+i
for i in e:
    sp=sp+i
print(sp)
 
