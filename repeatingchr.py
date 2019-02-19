s=input()
f=list(s)
e=[]
for i in range(len(s)):
    if s[i] not in e:
        e.append(s[i])
    else:
        print('yes')
        exit()
print('no')
