s=input()
l=list(s)
t=[]
q=0
for i in range(len(l)):
    if(l[i] not in t):
        t.append(l[i])
    else:
        z=len(t)
        if z>q:
            q=z
        t=[]
if q==0:
    print(len(s))
else:
    print(q)
        
           
