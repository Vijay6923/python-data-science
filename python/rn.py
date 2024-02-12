x=int(input("enter the four digit number: "))
a=x%10
num=x//10
b=num%10
num1=num//10
c=num1%10
d=num1//10
rev=(a*1000+b*100+c*10+d)
print(rev)
if x==rev:
    print(True)
else:
    print(False)