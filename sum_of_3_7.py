import sys
n=int(input())
if n%3==0 or n%7==0:
    print('yes')
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            q=7*i+3*j
            if q==n:
                print('yes')
                sys.exit()
    print('no')
