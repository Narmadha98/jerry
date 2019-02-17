n=int(input())
l=list(map(int,input().split()))
s=[]
if n%2==0:
    for i in range(n//2):
        m1=max(l)
        s.append(m1)
        l.remove(m1)
        m2=min(l)
        s.append(m2)
        l.remove(m2)
    print(*s)
else:
    for i in range(n//2):
        m1=max(l)
        s.append(m1)
        l.remove(m1)
        m2=min(l)
        s.append(m2)
        l.remove(m2)
    s.append(l[0])
    print(*s)
    

    
