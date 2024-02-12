n=int(input("enter the number: "))
a=n%10
num=n//10
b=num%10
c=num//10
x=(a**3+b**3+c**3)
print(x)
if x==n:
    print("the number is armstrong number")
else:
    print("the number is not armstrong number")