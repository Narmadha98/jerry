n=int(input())
l=list(map(int,input().split()))
f=0
s=l[0]
c=0
k=[]
for i in range(1,n):
    if(s==l[i]):
        if(f==0):
            f=1
            c=c+1
        else:
            c=c+1
    else:
        k.append(c)
        f=0
        s=l[i]
        c=0
k.append(c)
for i in range(len(k)):
    k[i]=k[i]+1
print(max(k))
            
    
