n=int(input())
a=list(map(int,input().split()))
m=max(a)
b=0
c=0
for i in range(0,n-1):
    for j in range(i+1,n):
            if abs(a[i]+a[j])<m:
                m=abs(a[i]+a[j])
                b=a[i]
                c=a[j]
print(b,c)
                
            
               
