n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
d=[]
for i in l:
    if(i<n):
        d.append(i)
print(*d)
#lkzxllkzx
