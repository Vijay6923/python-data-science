import math
x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))
x=[x1,y1]
y=[x2,y2]
print("Euclidean distan between two given co-ordinate is ",round(math.dist(x,y),2))