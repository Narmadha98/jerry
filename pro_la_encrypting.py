s=input()
x=input()
a=""
for i in range(len(s)):
    k=ord(x[i])-97+1
    if(ord(s[i])>=65 and ord(s[i])<=90):
            m=chr(((ord(s[i])-65+k)%26)+65)
            a=a+m
    elif(ord(s[i])>=97 and ord(s[i])<=122):
            n=chr(((ord(s[i])-97+k)%26)+97)
            a=a+n
print(a)
        
