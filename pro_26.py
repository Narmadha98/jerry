c=1
fg=0
n=int(input())
l=list(map(int,input().split()))
x=[]
for i in range(n-1):
  if l[i]<=l[i+1]:
    x.append(1)
  else:
    x.append(0)
for i in x:
  if fg<c:
    fg=c
  if i==1:
    c=c+1
  else:
    c=1
if fg<c:
  fg=c
print(fg)
