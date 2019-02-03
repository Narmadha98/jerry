n=int(input())
l=list(map(int,input().split()))
s=[]
a=""
for i in range(0,len(l)):
    if(l[i]%2==0 and i%2==1):
        s.append(l[i])
    elif (l[i]%2==1 and i%2==0):
        s.append(l[i])
for i in s:
    a=a+str(i)+" "
print(a.strip())
    
 
