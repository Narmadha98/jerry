n,k=map(int,input().split())
l=list(map(int,input().split()))
s=[]
for i in range(0,n,2):
    s.append(min((l[i:k+i])))
print(max(s))
