def check(n):
    if(n%2==0):
        return 0
    else:
        return 1

#driver code
ch='y'
while(ch=='y' or ch=='Y'):
    val=int(input("Enter No : "))
    if(check(val)==1):
        print("Odd")
    else:
        print("Even")
    ch=(input("Do you want to check more no ? y/n : "))