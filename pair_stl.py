# your code goes here
input()
l=[]
a=list(map(int,input().split()))
x=sorted(a)
c=[]
for i in range(0,len(a)):
	for j in range(len(a)):
		if a[i]==x[j]:
			c.append(j)
for i in range(len(c)):
	c[i]=c[i]+1
print(*c)
	
