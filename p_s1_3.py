x,y=map(str,input().split())
i=len(x)
j=len(y)
c=0
if(i<j):
    m=i
    ma=y
else:
    m=j
    ma=x
for i in range(m):
    if(x[i]==y[i]):
        c=c+1
    else:
        break
#print(ma)
#print(c)
print(len(ma)-c)


