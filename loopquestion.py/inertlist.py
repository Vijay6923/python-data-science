l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=[]
for i in l1:
    if i%2!=0:
        l3.append(i)
for i in l2:
    if i%2==0:
        l3.append(i)
print(l3)