def simple_interest(p, r, t):
    # Calculate the simple interest
    SI = (p*r*t)/100
    return SI
# driver code
p=int(input("Enter Principle : "))
r=float(input("Rate of interest : "))
t=int(input("time period : "))
print("Simple Interest : ",simple_interest(p,r,t))