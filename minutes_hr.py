n=int(input())
if(n%60<60):
    print("0"+" "+str(n))
if(n%60==0):
    print(str(n//60))
if(n>60):
    print(str(n//60)+" "+str(n%60))
    
