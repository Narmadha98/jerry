n=int(input())
f=n*5
if(n==0):
	print("0 0 0 0 0")
else:
    for i in range(1,6):
            if(i*n==f):
                    print(i*n)
            else:
                    print(i*n,end=" ")
