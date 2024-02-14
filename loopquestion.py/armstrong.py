armstrong_list=[]
for i in range (100,1000):
    a=i%10
    num=i//10
    b=num%10
    c=num//10
    if(a**3)+(b**3)+(c**3)==i:
        armstrong_list.append(i)
print(armstrong_list)