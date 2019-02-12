n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)-1):
	if (l[i]-l[i+1])>0:
		print(l[i])
		break
#abcdefghijklmnopqrstuvwxyz
