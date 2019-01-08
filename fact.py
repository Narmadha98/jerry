def fact(m):
    f=1
    for i in range(1,m+1):
        f=f*i
    return f
m=int(input())
if(m>=0):
    x=fact(m)
    print(x)
else:
    print(-1)
