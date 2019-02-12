input()
l=list(map(int,input().split()))
o=[]
e=[]
for i in range(len(l)):
    if l[i]%2==1:
        o.append(l[i])
    else:
        e.append(l[i])
if len(o)>len(e):
    print(e[0])
else:
    print(o[0])
