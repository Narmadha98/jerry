n,k=map(int,input().split())
a=list(map(int,input().split()))
w=set(a)
w=list(w)
w=sorted(w,reverse=True)
#print(w)
print(w[k-1])

