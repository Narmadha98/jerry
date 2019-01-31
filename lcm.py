a,b=map(int,input().split())

if(a>b):
    min1=b
else:
    min1=a
while(1):
    if(min1%a==0 and min1%b==0):
        print(min1)
        break
    min1=min1+1
#njdmb
