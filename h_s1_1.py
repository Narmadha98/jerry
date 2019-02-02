n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if(l.count(i)>1):
        r.append(i)
s=set(r)
s=list(s)
print(sorted(s))

    
       
