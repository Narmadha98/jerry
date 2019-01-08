n=int(input())
c=1
for i in range(2,n//2):
	if(n%i==0):
		c=0
		break
if(c==1):
	print("yes")
else:
	print("no")
	
	
