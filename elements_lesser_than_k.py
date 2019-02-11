# your code goes here
n,k=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
d=[]
for i in l:
	if(i<k):
		d.append(i)
print(*d)
