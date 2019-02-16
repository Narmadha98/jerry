import sys
s=input()
if s==s[::-1]:
  print('yes')
  sys.exit()
else:
  i=len(s)-1
  c=0
  for i in range(i,-1,-1):
    if s[i]=='0':
      c=c+1
    else:
      break
  s=s[:-c]
#print(c)
#print(s)
if s==s[::-1]:
  print('yes')
  sys.exit()
print('no')
    
