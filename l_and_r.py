def isPrime(n):
    c=1
    for i in range(2,n):
        if(n%i==0):
            c=0
            break
    return c
n,m=map(int,input().split())
s=0
c=1
for i in range(n,m+1):
    keerthi=isPrime(i)
    if(keerthi==1):
        s=s+1
print(s)
        

#prime between l and r
