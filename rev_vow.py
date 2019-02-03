l=int(input())
s=input()
s=list(s)
f=""
v=['a','e','i','o','u']
for i in s:
    if i in v:
        s.remove(i)
for i in s:
    f=f+i
print(f[::-1])

        
