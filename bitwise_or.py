n=int(input())
s=list(map(int,input().split()))
an=s[0]
for i in range(1,n):
    an=an|s[i]
print(an)
#bitwise_or
    
