input()
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    for j in range(len(a)):
        q=abs(a[i]-a[j])
        b.append(q)
print(max(b))
        
