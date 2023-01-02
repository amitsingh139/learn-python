import math

def quad(a,b,c):
    d=(b*b)-(4*a*c)
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("The roots are ",x1,x2)

# driver code
a=int(input("Enter coefficient of x^2 "))
b=int(input("Enter coefficient of x^1 "))
c=int(input("Enter coefficient of x^0 "))
quad(a,b,c)