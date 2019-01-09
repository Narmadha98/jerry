n=int(input())
if(n>60):
    print(str(n//60)+" "+str(n%60))
elif(n%60<60):
    print("0"+" "+str(n))
elif(n%60==0):
    print(str(n//60))
