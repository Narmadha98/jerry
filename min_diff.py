input()
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    for j in range(len(a)):
        q=abs(a[i]-a[j])
        b.append(q)
for i in b:
    if i==0:
        b.remove(0,)
print(min(b))
    
        
