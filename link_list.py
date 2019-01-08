def delete_first_element(l):
    del l[0]
    return l
def delete_last_element(l):
    del l[-1]
    l[len(l)-1][1]=0
    return l
def dele(l,i):
    for k in range(1,4):
        if(i==l[k][0]):
            l[k-1][1]=l[k][1]
            del l[k]
    return l
l=[[1,1000],[2,1002],[3,1003],[4,1005],[5,0]] #0-for_null
s=dele(l,2)  
print(s)
k=delete_first_element(l)
print(k)
m=delete_last_element(l)
print(m)
