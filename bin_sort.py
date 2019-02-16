n=int(input())
l=list(map(int,input().split()))
c=[[x,bin(x),str(bin(x)).count('1')] for x in l]
s=sorted(c,key=lambda x:x[2],reverse=True)
for i in s:
    del i[1]
for i in s:
    print(i[0])
               
#hi guviii:)
