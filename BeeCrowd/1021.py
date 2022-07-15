
balance=float(input())
print("NOTAS:")
for i in [100.00,50.00,20.00,10.00,5.00,2.00]:
    b=int(balance//i)
    print(f'{b} nota(s) de R$ {i:.2f}')
    # print(balance%i)
    balance=float(f'{balance%i:.2f}')
    # print(balance)

print("MOEDAS:")
for i in [1.00,0.50,0.25,0.10,0.05,0.01]:
    c=(balance//i)
    # print(c)
    print(f'{c} moeda(s) de R$ {i:.2f}')
    balance=float(f'{balance%i:.2f}')
    # print(balance)
