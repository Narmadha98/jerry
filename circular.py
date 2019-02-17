n=0
e=1
s=2
w=3
def CircularPath(s):
    x=0
    y=0
    d=n
    for i in range(len(s)):
        move=s[i]
        if move=='R':
            d=(d+1)%4
        elif move=='L':
            d=(d+3)%4
        else:
            if d==0:
                y=y+1
            elif d==2:
                y=y-1
            elif d==1:
                x=x+1
            elif d==3:
                x=x-1
    return x,y
s=input()
d=CircularPath(s)
if d==(0,0):
    print('yes')
else:
    print('no')
