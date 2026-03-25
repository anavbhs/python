passageiros = ["Ana","Bruno","Carlos","Daniela","Eduardo"]
#Exercício 01
print('Passageiros do voo:')
for passageiro in passageiros:
    print(passageiro)
print()
#Exercício 02
# for passageiro in passageiros:
#     print(f'{passageiro} realizou o check-in')
# print()
#Exercício 03
for passageiro in passageiros:
    if passageiro == 'Carlos':
        print(f'{passageiro} perdeu o check-in')
    else:
        print(f'{passageiro} realizou o check-in')
print()
#Exercício 04
for passageiro in passageiros:
    if passageiro == 'Daniela' or passageiro == 'Eduardo':
        break
    print(f'{passageiro} pode embarcar')
print()
#Exercício 05
for num_passageiro in range(len(passageiros)):
    print(f'Passageiro {num_passageiro + 1}: {passageiros[num_passageiro]}')