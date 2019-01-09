n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
a=0
b=len(s)-1
if(len(s)%2==1):
    mid=(a+b)//2
    print(l[mid])
else:
    c=n-1//2
    d=n//2
    print((c+d)//2)
  
  
