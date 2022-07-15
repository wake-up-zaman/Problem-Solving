from cmath import sqrt

import math
x1,y1=[float(x) for x in input("").split()]
x2,y2=[float(x) for x in input("").split()]
A=pow((x2-x1),2)
B=pow((y2-y1),2)
C=math.sqrt(A+B)
print(f"{C:.4f}")
