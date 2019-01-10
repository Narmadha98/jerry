s=input()
c=0
a=["!","@","#","$","%","^","&","*","(",")"]
for i in s:
    if(i in a):
        c=c+1
print(c)
