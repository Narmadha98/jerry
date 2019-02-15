n,q=map(int,input().split())
l=list(map(int,input().split()))
a=[]
s=[]
while(q!=0):
    u,v=map(int,input().split())
    for j in range(u,v+1):
        a.append(l[j-1])
    s.append(sum(a))
    a=[]
    q=q-1
for e in s:
    print(e)


    

