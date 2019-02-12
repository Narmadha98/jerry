from itertools import combinations
n,k=map(str,input().split())
k=int(k)
n=list(n)
p=list(combinations(n,len(n)-k))
m=min(p)
st=""
for i in m:
    st=st+i
print(st)

