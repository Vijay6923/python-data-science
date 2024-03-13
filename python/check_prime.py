def is_prime(number):
    return number >1 and all (number % i !=0 for i in range (2,int(number**0.5) +1))
num=int(input("enter the number: "))
print(f"{num} is {'prime' if is_prime(num) else'not prime'}.")