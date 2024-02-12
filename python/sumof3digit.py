def mod(a,b,m):
    if(b==0):
        return 1
    else:
        return ((a%m)*(mod(a,b-1,m)))%m
a=int(input())
b=int(input())
m=int(input())
print(mod(a,b,m))


