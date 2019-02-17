n=int(input())
j=list(map(int,input().split()))
s=0
for i in range(n):
    if j[i]<0:
        s=s+j[i]
print(s)
#sum_of_neg       
