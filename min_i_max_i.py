n=int(input())
l=list(map(int,input().split()))
min1=min(l)
max1=max(l)
#print(min1,max1)
for i in range(0,n):
  if min1==l[i]:
    i1=i
    break
for i in range(0,n):
  if max1==l[i]:
    i2=i
    break
#print(i1,i2)
print(abs(i2-i1))
