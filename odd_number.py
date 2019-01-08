n,m=map(int,input().split())
for i in range(n+1,m):
	if(i!=m-1):
		if(i%2==1):
			print(i,end='')
	else:
		if(i%2==1):
			print(i)
