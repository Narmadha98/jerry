n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
    if(l[i]==i):
        s.append(i)
if(len(s)==0):
    print("-1")
else:
    s=sorted(s)
    print(*s)

        
       
