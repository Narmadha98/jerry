x=int(input())
s=""
for i in range(1,x+1):
    if(x%i==0):
        s=s+str(i)+" "
print(s.strip())
