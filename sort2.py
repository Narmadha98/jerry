c=[0]*100000
n=int(input())
l=[]
s=""
k=list(map(int,input().split()))
for a in k:
    c[a]+=1
for i in range(max(k)+1):
    while(c[i]>0):
        s=s+str(i)+" "
        c[i]-=1
print(s.strip())
