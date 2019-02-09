p,a=map(int,input().split())
m=p//2
c=0
for i in range(m,0,-1):
    for j in range(0,m):
        if i+j==m and i*j==a:
            print('yes')
            c=1
            break
    if c==1:
        break
else:
    print('no')
