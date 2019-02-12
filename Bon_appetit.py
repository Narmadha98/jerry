n,k=map(int,input().split())
l=list(map(int,input().split()))
amt=int(input())
s=sum(l)
b=amt-(s-l[k])/2
if b==0:
    print("Bon Appetit")
else:
    print(int(b))
