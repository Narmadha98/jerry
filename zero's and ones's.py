n=input()
s=input()
q=""
m=0
for i in range(0,len(s)):
  if s[i]=="0":
    q=q+s[m:i]
    m=i+1
q=list(q)
print(*q)
