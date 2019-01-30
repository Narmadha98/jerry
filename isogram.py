def isogram(s):
    x=s.lower()
    l=[]
    for i in x:
        if i in l:
            return False
        l.append(i)
    return True
s=input()
a=isogram(s)
if(a=="True"):
    print("Yes")
else:
    print("No")
