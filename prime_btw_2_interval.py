def isPrime(n):
    c=1
    for i in range(2,n//2):
        if(n%i==0):
            c=0
            break
    return c
n,m=map(int,input().split())
s=""
c=1
for i in range(n+1,m):
    keerthi=isPrime(i)
    if(keerthi==1):
        s=s+str(i)+" "
print(s.strip())
        
