n,k=map(int,input().split())
if n==0:
    print("no")
while n!=1:
    if n%k!=0:
        print("no")
        break
    n=n//k
else:
    print("yes")
#ksjv ns
