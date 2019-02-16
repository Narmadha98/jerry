import sys
n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if i!=j and l[i]+l[j]==k:
            print('yes')
            sys.exit(0)
print('no')
            
        
