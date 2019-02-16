import sys
n=int(input())
a=list(map(int,input().split()))
for i in range(1,n-1):
  x=a[0:i]
  y=a[i:]
  w=sum(x)//len(x)
  q=sum(y)//len(y)
  if w==q:
    print('yes')
    sys.exit()
print('no')
