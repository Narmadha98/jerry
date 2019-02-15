n=int(input())
a=list(map(int,input().split()))
st=[]
for i in range(0,n):
    if all(a[i]>a[k] for k in range(i+1,n)):
        st.append(a[i])
print(*st)
print(max(a))
    
