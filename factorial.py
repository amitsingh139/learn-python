def fact(n):
    f=1
    for i in range(1,n + 1):    
       f = f*i    
    return f

# driver code
val=int(input("Enter No : "))
print("Factorial : ",fact(val))