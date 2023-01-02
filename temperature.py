def temp(c):
    f=((9*c)/5)+32
    return f

# driver code
c=float(input("Enter temperature in celcius : "))
print("Temperature in Fahrenheit : ",temp(c))