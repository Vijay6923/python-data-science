p=float(input("principle amount: "))
r=float(input("rate of interest: "))
t=int(input("for thr time period: "))
simple_interest=(p*r*t)/100
print(simple_interest)
totaldue=p+simple_interest
print("Total due amount will need to pay will be",totaldue)