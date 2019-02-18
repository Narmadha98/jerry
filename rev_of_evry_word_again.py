l=list(map(str,input().split()))
w=[]
for i in range(0,len(l)):
    if((i+1)%2==1):
        f=l[i]
        w.append(f[::-1])
    else:
        w.append(l[i])
sp=""
for i in w:
    sp=sp+i+" "
print(sp)
                
