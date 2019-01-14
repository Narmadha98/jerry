a=input()
c=["True" if i in ('0','1') else "False" for i in a]
flag=0
for i in c:
    if i=="False":
        flag=1
if(flag==0):
    print("yes")
else:
    print("no")
        
    
