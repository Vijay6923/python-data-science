n=int(input("enter the 4 digit number: "))
a=n%10
num=n//10
b=num%10
num1=num//10
c=num1%10
d=num//10
x=(a**4+b**4+c**4+d**4)
if x==n:
    print("the number is narcissist number")
else:
    print("the number is not narcissist number")
