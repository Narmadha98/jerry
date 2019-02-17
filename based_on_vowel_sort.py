x=int(input())
s=[]
for i in range(x):
    s.append(input())
v=['a','e','i','o','u','A','E','I','O','U']
c=0
e=[]
g=[]
y=[]
#print(s)
for i in s:
    #print(i)
    for k in range(len(i)):
        #print(i[k])
        if i[k] in v:
            c=c+1
    e=[i,c]
    g.append(e)
    c=0
#print(g)
y=sorted(g,key=lambda x: x[1],reverse=True)
#print(y)
for i in y:
    print(i[0])
