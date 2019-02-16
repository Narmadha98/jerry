a,b=map(str,input().split())
#d=len(a)-len(b)
#d=abs(d)
d=0
if len(a)>len(b):
    mins=b
    maxs=a
elif len(a)<len(b):
    mins=a
    maxs=b
else:
    mins=a
    maxs=b
for i in range(0,len(mins)):
    if a[i]==b[i]:
        continue
    else:
        d=d+abs(ord(a[i])-ord(b[i]))
while(i+1<len(maxs)):
    d=d+ord(maxs[i+1])-96
    i=i+1
print(d)
