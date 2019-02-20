n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
l=l[::-1]
A_has=0
B_has=0
for i in l:
    d=A_has+i
    if B_has>d:
        A_has=d
    else:
        A_has=B_has
        B_has=d
print(A_has,B_has)
