n=int(input())
s=""
l=list(map(int,input().split()))
l=sorted(l,reverse=True)
for i in l:
    s=s+str(i)
if l.count(0)==len(l):
    print("0")
else:
    print(s)
