n=int(input())
l=[]
f=1
s=1
for i in range(n):
    l.append(list(map(int,input().split())))
#print(l)
for i in range(n):
    f=f*l[i][i]
    #print(l[i][i],f)
for j in range(n):
    s=s*l[j][n-j-1]
    #print(l[j][n-j-1],s)
print(s+f)
             
        
