k=int(input())
w=[]
for i in range(k):
    l=list(map(int,input().split()))
    for j in l:
        w.append(j)
s=sorted(w)
print(*s)
