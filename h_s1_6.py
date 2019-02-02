#from collections import Counter
n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
c=[]
#print(s)
for i in l:
    if(l.count(i)>1):
        print(i)
        break
else:
    print('unique')

    
       
