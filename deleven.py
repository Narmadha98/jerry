def deleven(z):
    m=[]
    for i in range(0,len(z)):
        if i%2==1:
            m.append(z[i])
    return m
n=int(input())
l=list(map(int,input().split()))
s=l
while(len(l)!=1):
    l=deleven(l)
#print(l)
print(s.index(l[0]))
