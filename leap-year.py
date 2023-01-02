def year_fun(y):
    if(y%400==0):
        return 1
    elif(y%4==0):
        return 1
    return 0

#Driver Code
val=int(input("Enter Year : "))
if(year_fun(val)==1):
    print("Leap Year")
else:
    print("Not Leap Year")     