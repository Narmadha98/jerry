from itertools import combinations
import sys
s=input()
a=list(combinations(s,len(s)-1))
for i in  range (len(a)):
    p=a[i]
    if p==p[::-1]:
        print('yes')
        sys.exit()
print('no')
