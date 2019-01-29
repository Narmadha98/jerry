a=input()
s=list(a)
n=len(s)
if(n%2==0):
    s[n//2-1]="*"
    s[n//2]="*"
else:
    s[n//2]="*"
s1=""
for i in s:
    s1=s1+i
print(s1)
