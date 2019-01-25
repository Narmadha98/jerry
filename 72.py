s=input()
l=['a','e','i','o','u']
c=0
for i in s:
    if i in l:
        c=1
if c==1:
    print("yes")
else:
    print("no")
