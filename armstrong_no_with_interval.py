n,m=map(int,input().split())
s2=""
for i in range(n+1,m):
    temp=i
    s=0
    while(i>0):
        re=i%10
        s+=re*re*re
        i=i//10
    if(temp==s):
        s2=s2+str(s)+" "
        s=0
    else:
        s=0
print(s2.strip())
