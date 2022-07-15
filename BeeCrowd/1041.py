A,B=[float(x) for x in input("").split()]
if(A==0.0 and B==0.0):
    print('Origem')
if(A>0.0 and B>0.0):
    print('Q1')
if(A<0.0 and B>0.0):
    print('Q2')
if(A<0.0 and B<0.0):
    print('Q3')
if(A>0.0 and B<0.0):
    print('Q4')
if((A>0.0 and B==0.0) or (A<0.0 and B==0.0)):
    print('Eixo X')
if((B>0.0 and A==0.0) or (B<0.0 and A==0.0)):
    print('Eixo Y')



