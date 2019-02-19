n=int(input())
l=list(map(str,input().split()))
for i in range(0,n-1,2):
    l[i],l[i+1]=l[i+1],l[i]
sp=""
for i in l:
    sp=sp+i+" "
print(sp.strip())
    
