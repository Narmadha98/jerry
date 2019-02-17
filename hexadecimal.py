import string
s=input()
f=all(c in string.hexdigits for c in s)
if(f):
    print('yes')
else:
    print('no')
#hexdecimal
