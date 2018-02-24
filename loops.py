hrs = input("Enter Hours:")
h=float(hrs)

if(h<=40):
    rate=float(input("enter the rate per hour"))
    pay=h*rate
    print(pay)
else:
    rate=float(input("enter the rate per hour"))
    r=rate*1.5
    pay=h*r
    print(pay)