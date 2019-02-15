n=int(input())
p=0
for i in range(1,n):
    for j in range(i,n+1):
        if i!=j:
            p=p+1
print(p)
