n,m=map(int,input().split())
for i in range(n+1,m):
    temp=i
    s=0
    while(i>0):
        re=i%10
        s+=re*re*re
        i=i//10
    if(temp==s):
        print(s,end=" ")
print(end="\n")
