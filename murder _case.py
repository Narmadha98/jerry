n=int(input())
a=list(map(int,input().split()))
z=[]
for i in range(1,n):
    for j in range(0,i):
        if(a[i]>a[j]):
            z.append(a[j])
print(sum(z))
#hi guvii:"{
