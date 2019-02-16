s=int(input())
l=list(map(int,input().split()))
flag=0
lencounter=1
p=[]
for i in range(s-1):
    if l[i]<l[i+1]:
        if flag==0:
            flag=1
            lencounter=1
        else:
            lencounter+=1
    else:
        if flag==1:
            p.append(lencounter+1)
        flag=0
if flag==1:
    p.append(lencounter+1)
print(max(p))
