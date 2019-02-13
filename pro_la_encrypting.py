a=input()
b=input()
i=0
n=len(a)
sp=""
while(i<n):
        k=ord(a[i])-97+1
        l=ord(b[i])-97+1
        print(k,l)
        if k==l:
            w=k+97-1
            sp=sp+chr(w)
        elif(k+l<=26):
            g=(k+l)+97-1
            k=chr(g)
            sp=sp+k
        else:
            y=(k+l)%26
            z=y+97-1
            k=chr(z)
            sp=sp+k
        i=i+1
print(sp)
        
    
        
