A,B,C,D=[float(x) for x in input("").split()]
Average=(A*2+B*3+C*4+D*1)/(2+3+4+1)

if(Average>=7.0):
    print(f"Media: {Average:.1f}")
    print('Aluno aprovado.')
elif(Average<5.0):
    print(f"Media: {Average:.1f}")
    print('Aluno reprovado.')
elif(Average>=5.0 and Average<=6.9):
    E=float(input(''))
    Average2=(Average+E)/2
    print(f"Media: {Average:.1f}")
    print("Aluno em exame.")
    print(f'Nota do exame: {E:.1f}')
    if(Average2>=5.0):
        print('Aluno aprovado.')
    elif(Average2<=4.9):
        print('Aluno reprovado.')
    print(f"Media final: {Average2:.1f}")

