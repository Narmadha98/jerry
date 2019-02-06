x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
if x1==y1 and x2==y2 and x3==y3:
    print("yes")
elif x1==x2 and x1==x3:
    print("yes")
elif y1==y2 and y1==y3:
    print("yes")
else:
    print("no")
#print kdls
