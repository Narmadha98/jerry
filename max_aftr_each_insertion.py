n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=""
for i in b:
    a.append(i)
    m=m+str(max(a))+" "
print(m.strip())
#hey guvi    
