a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[2,4,6],[8,10,12],[14,16,18]]
c=[[1,3,6],[9,12,15],[18,21,24]]

for i in range (3):
    for j in range (3):
        sum=0
        for p in range (3):
            sum +=a[i][p]*b[i][p]

i,j=0,0
for i in range (3):
    for j in range (3):
        print(c[i][j],end=" ")
    print( )