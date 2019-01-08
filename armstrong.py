n=int(input())
te=n
s=0
while(te>0):
    re=te%10
    s+=re*re*re
    te=te//10
if(s==n):
    print("yes")
else:
    print("no")
    
