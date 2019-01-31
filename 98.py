# your code goes here
n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
for i in range(0,len(l)):
	if(l[i]!=s[i]):
		print(i)
		break
