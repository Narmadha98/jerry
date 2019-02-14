# your code goes here
input()
l=[]
a=list(map(int,input().split()))
for i in range(0,len(a)-1):
	s=a[i]+a[i+1]
	l.append(s)
print(sum(l))
	
