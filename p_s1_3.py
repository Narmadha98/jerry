a,b=map(str,input().split())
d=len(a)-len(b)
d=abs(d)
a=list(a)
b=list(b)
i=0
j=0
while  i<len(a) and j<len(b):
    if(a[i]==b[j]):
        i=i+1
        j=j+1
    else:
        if(len(a)>len(b)):
            a.pop(i)
        else:
            i=i+1
            j=j+1
            d=d+1
print(d)
            
        
    

