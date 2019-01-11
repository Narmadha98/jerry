s=input()
a=""
w=s[0].upper()
a=a+w
i=1
while(i<len(s)):
    if(s[i]==' '):
        r=s[i+1].upper()
        a=a+" "+r
        i=i+2
    else:
        a=a+s[i]
        i=i+1
print(a)
        
        
