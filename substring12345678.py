s,a=map(str,input().split())
if(len(s)<len(a)):
    mi=s
else:
    mi=a
x=len(mi)
for i in range(0,x+1):
        w=mi[0:i]
        if w in s:
            b=w
print(b)
    
        
    
