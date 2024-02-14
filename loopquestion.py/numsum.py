n=int(input("enter the number: "))
prev_num=0
for i in range(n):
    x=prev_num+i
    prev_num=i
    print(x,end=" ")