n=int(input())
x=[]
for i in range(n):
    c=list(map(int,input().split()))
    x.append(c)
p=0
for i in range(n):
    for j in range(n):
        if i==j:
            p=p+x[i][j]
print(p)
