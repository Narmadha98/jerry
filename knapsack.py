n,w=map(int,input().split())
we=list(map(int,input().split()))
va=list(map(int,input().split()))
s=0
op=0
for i in range(n):
    s+=we[i]
    if w<s:
        break
    op+=va[i]
print(op)
    
