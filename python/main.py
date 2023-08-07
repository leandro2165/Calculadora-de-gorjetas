print('Calculadora de gorjetas: ')

opcao = int(input('\n Opção 1 - 20% Muito bom \n opção 2 - 10% Bom \n Opção 3 - 5% Ruim \n Digite: '))

if opcao == 1:
    conta_1 = float(input('Quanto ficou a conta? R$'))
    pessoas_1 = int(input('Quantas pessoas vão dividir? '))
    dividir_1 = (conta_1 * 20) / 100
    total_1 = dividir_1 / pessoas_1
    print(f'Gorjeta Total: R${total_1 :.2f} cada')
elif opcao == 2:
    conta_2 = float(input('Quanto ficou a conta? R$'))
    pessoas_2 = int(input('Quantas pessoas vão dividir? '))
    dividir_2 = (conta_2 * 10) / 100
    total_2  = dividir_2 / pessoas_2
    print(f'Gorjeta total: R${total_2 :.2f} Cada')
elif opcao == 3:
    conta_3 = float(input('Quanto ficou conta? R$'))
    pessoas_3 = int(input('Quantas pessoas vão dividir? '))
    dividir_3 = (conta_3 * 5) / 100
    total_3 = dividir_3 / pessoas_3
    print(f'Gorjeta total: R${total_3 :.2f} cada')
else:
    print('Erro...')
    