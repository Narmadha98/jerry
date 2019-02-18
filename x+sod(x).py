def digsum(i):
    s=0
    for k in range(len(i)):
        s=s+int(i[k])
    return s
n=int(input())
f=[]
for i in range(n):
    o=str(i)
    if(n==i+digsum(o)):
        f.append(i)
print(len(f))
if len(f)>0:
    for i in f:
        print(i)
else:
    print(-1)
