n=int(input())
s=list(map(int,input().split()))
p1=s[::2]
p2=s[1::2]
if sum(p1)>sum(p2):
  print(sum(p1))
else:
  print(sum(p2))
