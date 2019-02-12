n=int(input())
l=[]
z=0
for i in range(0,n):
    s=input()
    l.append(s)
q=[]
for i in l:
    q.append(len(i))
min1=min(q)
p=[]
for i in range(min1):
    for j in range(1,n):
        if(l[0][i]==l[j][i]):
            p.append(l[0][i])
            z=1
        else:
            z=0
            break
    if(z==0):
        break
p=set(p)
p=sorted(p)
x1=[]
for i in l:
    if len(i)==min1:
        a1=i
        break
for i in range(min1):
    for j in range(len(p)):
        if a1[i]==p[j]:
             x1.append(a1[i])
             
m=""
for i in x1:
    m=m+i
print(m)


            
            
        
