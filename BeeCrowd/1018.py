balance=int(input(""))
if balance>0 and balance<1000000:
    notes_100=int(balance/100)
    rb_100=balance%100
    notes_50=int(rb_100/50)
    rb_50=rb_100%50
    notes_20=int(rb_50/20)
    rb_20=rb_50%20
    notes_10=int(rb_20/10)
    rb_10=rb_20%10
    notes_5=int(rb_10/5)
    rb_5=rb_10%5
    notes_2=int(rb_5/2)
    rb_2=rb_5%2
    notes_1=int(rb_2/1)
    print(balance)
    print(f'{notes_100} nota(s) de R$ 100,00')
    print(f'{notes_50} nota(s) de R$ 50,00')
    print(f'{notes_20} nota(s) de R$ 20,00')
    print(f'{notes_10} nota(s) de R$ 10,00')
    print(f'{notes_5} nota(s) de R$ 5,00')
    print(f'{notes_2} nota(s) de R$ 2,00')
    print(f'{notes_1} nota(s) de R$ 1,00')

