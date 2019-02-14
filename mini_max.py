# your code goes here
input()
a=list(map(int,input().split()))
s=sum(a)
so=sorted(a)
print(s-so[0])
