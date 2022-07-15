x, y, z = [int(x) for x in input("").split()]
A=(x+y+abs(x-y))/2
B=(A+z+abs(A-z))/2
print(int(B),"eh o maior")