
#catalan_numbers
#Cn+1=C0Cn+C1Cn+....+CnC0
def catalan(n):
    if n<=1:
        return 1
    else:
        s=0
        for i in range(n):
            s=s+catalan(i)*catalan(n-i-1)
        return s
n=int(input())
if n==0:
    n=1
c=[]
for i in range(n):
    c.append(catalan(i))
print(*c)
