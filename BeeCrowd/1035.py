# A,B,C,D=[int(x) for x in input("").split()]
# sum1=C+D
# sum2=A+B
# if B>C and D>A and sum1>sum2 and C>0 and D>0 and A%2==0:
#     print('Valores aceitos')
#     # if sum1>sum2:
#     #     if C>0 and D>0:
#     #         if A%2==0:
#                 # print('Valores aceitos')
# else:
#     print('Valores nao aceitos')

A,B,C,D=[int(x) for x in input("").split()]
sum1=C+D
sum2=A+B
if B>C and D>A:
    if sum1>sum2:
        if C>0 and D>0:
            if A%2==0:
                print('Valores aceitos')
            else:
                print('Valores nao aceitos')
        else:
            print('Valores nao aceitos')
    else:
        print('Valores nao aceitos')
else:
    print('Valores nao aceitos')