n1,n2=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if all( i in a for i in b):
    print("YES")
else:
    print("NO")
  
       
