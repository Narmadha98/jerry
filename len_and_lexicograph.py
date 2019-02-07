n=int(input())
l=list(map(str,input().split()))
p=sorted(l,key=len)
#print(*p)
for i in range(n-1):
    if(len(p[i])==len(p[i+1])):
        a=p[i]
        b=p[i+1]
        for x in range(len(p[i])):
            if a[x]<b[x]:
                break
            elif a[x]>b[x]:
                p[i],p[i+1]=p[i+1],p[i]
                break
print(' '.join(p))


  
