def isPrime(n):
    c=1
    for i in range(2,n):
        if(n%i==0):
            c=0
            break
    return c
m=int(input())
s=0
c=1
for i in range(2,m):
    keerthi=isPrime(i)
    if(keerthi==1):
        k=str(i)
        x=len(k)
        if (k[x-1]=='3'):
            s=s+int(i)
print(s)
