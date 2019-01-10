n=int(input())
t1=1
t2=1
s=""
for i in range(1,n+1):
    s=s+str(t1)+" "
    nextT=t1+t2
    t1=t2
    t2=nextT
print(s.strip())
    
