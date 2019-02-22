n,p,q,r=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i<=j and j<=k:
                a.append(p*l[i]+q*l[j]+r*l[k])
                
print(max(a))
