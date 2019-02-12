# your code goes here
n=int(input())
l=list(map(int,input().split()))
x=[]
for i in range(0,n-1):
	x.append(max(l[i],l[i+1]))
print(*x)
	
