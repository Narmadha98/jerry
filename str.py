s=input()
o=""
e=""
for i in range(len(s)):
    if(i%2==0):
        o=o+s[i]
    else:
        e=e+s[i]
print(o+" "+e)

        
