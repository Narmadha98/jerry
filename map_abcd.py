n=int(input())
s=str(n)
c=0
for i in range(0,len(s)):
    if int(s[i:i+2])<26 and len(str(int(s[i:i+2])))==2:
        c=c+1
if c==2:
    print(c+c//2)
else:
    print(c+c//2+1)


    
