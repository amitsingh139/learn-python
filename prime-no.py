def prime(n):
    if(n==2):
        return 1          
    else:
        for i in range(2,n):
            if(n%i==0):
                return 0
        return 1

# driver code
ch='y'
while(ch=='y' or ch=='Y'):
    val=int(input("Enter No : "))
    if(prime(val)==1):                 # 1: prime no                    
        print("Prime No")              # 0: Composite no 
    else:
        print("Composite")
    ch=input("Do you want to check more ? y/n : ")    