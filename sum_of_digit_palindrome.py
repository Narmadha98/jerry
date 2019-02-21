def sod(s):
    x=0
    for i in s:
       x=x+int(i)
    return x
s=input()
c=sod(s)
c=str(c)
if c==c[::-1]:
    print("YES")
else:
    print("NO")
        

