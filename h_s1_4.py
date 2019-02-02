n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    z= l.count(i)
    if(z==1):
        print(i)
        break
       
