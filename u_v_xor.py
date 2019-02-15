n,q=map(int,input().split())
l=list(map(int,input().split()))
s=[]
xor=0
while(q!=0):
    u,v=map(int,input().split())
    for j in range(u,v+1):
        xor=xor^l[j-1]
    s.append(xor)
    q=q-1
    xor=0
for e in s:
    print(e)


    

