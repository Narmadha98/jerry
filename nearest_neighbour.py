n,k=map(int,input().split())
l=list(map(int,input().split()))
o=[]
r=[[abs(i-k),i] for i in l]
p=sorted(r)
p.pop(0)
#print(p)
for i in range(3):
    o.append(p[i][1])
print(*o)
