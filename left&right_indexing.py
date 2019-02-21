n=int(input())
s=list(map(int,input().split()))
for i in range(0,n):
    if sum(s[:i])==sum(s[i+1:]):
        print('yes')
        exit()
print('no')
        
    
