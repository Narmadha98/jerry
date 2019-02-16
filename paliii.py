st=input()
n=len(st)
c=0
for i in range(len(st)-1):
    if st[i]!=st[n-i-1]:
        c=c+1
    #print(c)
if c<=1:
    print('yes')
else:
    print('no')
 
