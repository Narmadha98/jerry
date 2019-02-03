s=input()
s=list(s)
c=[0]*256
for i in range(len(s)):
    c[ord(s[i])]=s.count(s[i])
m=max(c)
for i in range(256):
    if(m==c[i]):
        print(chr(i))
        
