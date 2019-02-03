s=input()
a=""
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        i=chr(((ord(i)-65+3)%26)+65)
        a=a+i
    elif(ord(i)>=97 and ord(i)<=122):
        i=chr(((ord(i)-97+3)%26)+97)
        a=a+i
    
print(a)
        
        
