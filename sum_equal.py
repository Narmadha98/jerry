n,x=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,n):
  for j in range(i+1,n):
    if l[i]+l[j]==x:
      print ("yes")
      break
else:
  print("no")
  
  
