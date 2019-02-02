n=int(input())
l=list(map(int,input().split()))
s=l[::-1]
a=""
b=""
for i in range(len(s)):
    a=a+str(s[i])+"->"
#print(a)
a1=list(a)
a1.pop(len(a)-1)
a1.pop(len(a1)-1)
for i in a1:
    b=b+str(i)
print(b)

