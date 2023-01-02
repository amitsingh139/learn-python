def sum(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s


#driver code
val=int(input("Enter No : "))
print("Sum : ",sum(val)) 