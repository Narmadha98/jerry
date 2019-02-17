s=input()
l=[]
l=s.split(" ")
s1=""
for i in range(len(l)):
    s=l[i]
    s1=s1+s[::-1]+" "
print(s1.strip())
#reverse every wordldnckca
