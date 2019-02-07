def binsearch(l,f,e,k):
    mid=(f+e)//2
    while(f<=e):
        if l[mid]==k:
            return mid
        elif l[mid]>k:
            return binsearch(l,f,mid-1,k)
        else:
            return binsearch(l,mid+1,e,k)
    else:
        return -1
n,k=map(int,input().split())
l=list(map(int,input().split()))
r=binsearch(l,0,n-1,k)
if r!=-1:
    print("Yes")
else:
    print("No")
