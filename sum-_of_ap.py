a,d,n=map(int,input().split())
sum=0
for i in range(0,n):
	sum=sum+a
	a=a+d
print(sum)
