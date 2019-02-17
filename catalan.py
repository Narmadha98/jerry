def catalan(n):
  if n<=1:
    return 1
  else:
    r=0
    for i in range(n):
      r+=catalan(i)*catalan(n-i-1)
    return r
n=int(input())
if n<=1:
  n+=1
else:
  n=n
li=[]
for i in range(n):
  li.append(catalan(i))
print(*li)
