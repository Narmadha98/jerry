x=[]
n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    if l[i]<l[i+1]:
      x.append(1)
    else:
      x.append(-1)
if sum(x)==0:
  print('yes')
else:
  print('no')
