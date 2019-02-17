s=input()
l=""
for i in s:
    if(i.islower()):
        l=l+i.upper()
    elif(i.isupper()):
        l=l+i.lower()
    else:
        l=l+i
print(l)
#reverse case
        
