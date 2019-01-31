def rec(a):
    if(a%2!=0):
        print(a)
    else:
        a=a//2
        rec(a)
n=int(input())
s=rec(n)

