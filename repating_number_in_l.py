n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    s.append(l.count(i))
m=max(s)
for i in range(len(s)):
    if s[i]==m:
        print(l[i])
        break
        
       
