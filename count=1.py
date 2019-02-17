s=input()
p=[]
for i in s:
    x=s.count(i)
    if x==1:
        p.append(i)
sp=""
for i in p:
    sp=sp+i
print(sp)
    
