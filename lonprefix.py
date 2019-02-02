n=int(input())
l=[]
z=0
for i in range(0,n):
    s=input()
    l.append(s)
#print(l)
q=[]
for i in l:
    q.append(len(i))
#print(q)
min1=min(q)
#print(min1)
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
m=""
for i in p:
    m=m+i
print(m)
#myveryowncodexmvlxkvjm 

            
            
        
   

            
