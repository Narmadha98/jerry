def isPowerOf2(n):
    if(n==0):
        return False
    else:
        while(n!=1):
            if(n%2!=0):
                return False
            n=n/2
    return True
                
    



n=int(input())
if(isPowerOf2(n)):
    print("yes")
else:
    print("no")
