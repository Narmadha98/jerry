l=list(map(str,input().split()))
#print(l)
if all(l[i][0].isupper() for i in range(len(l))):
    print('yes')
else:
    print('no')
#camelcase
