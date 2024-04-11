x=10
if(x>1):
    for i in range(2,(x//2)+1):
        if (x%i)==0:
            print(x,'number is not prime')
            break
        else:
            print(x,'Number is  prime')
            break

