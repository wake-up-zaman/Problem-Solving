import math

A,B,C=[float(x) for x in input("").split()]

R1=(B*B)-4*A*C
if A==0:
    print('Impossivel calcular')

elif R1<0:
    print('Impossivel calcular')
    
else:
    Q1=float((-B+math.sqrt((B*B)-4*A*C))/(2*A))
    Q2=float((-B-math.sqrt((B*B)-4*A*C))/(2*A))
    print(f'R1 = {Q1:.5f}')
    print(f'R2 = {Q2:.5f}')