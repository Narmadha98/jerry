n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if(i!=j):
            if a[i]+a[j]==0:
                print(a[i],a[j])
                break
            
               
