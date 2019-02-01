n,k=map(int,input().split())
l=list(map(int,input().split()))
o=[]
for i in l:
	if i%2==1:
		o.append(i)
print(o[k-1])
 
