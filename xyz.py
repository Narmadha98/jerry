input()
l=list(map(int,input().split()))
n=len(l)
f=0
c=0
a=[]
for i in range(0,n-1):
	if l[i]<l[i+1]:
		if f==0:
			f=1
			c=c+1
			x=c
		else:
			c=c+1
			x=c
	else:
		a.append(c)
		c=0
		f=0
if i==n-1:
    a.append(x)
for i in range(len(a)):
    a[i]=a[i]+1
print(max(a))
    
