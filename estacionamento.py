valor=0
carros=0
motos=0
caminhonete=0
i=0
total=0

print('TIPO DE VEÍCULO  |   VALOR')
print('     MOTO        |  R$5,00')
print('     CARRO       | R$10,00')
print('   CAMINHONETE   | R$15,00')
print('\n')

while i == 0:


    print('======ESTACIONAMENTO======')
    print('1-Registrar moto')
    print('2-Registrar carro')
    print('3-Registrar caminhonete')
    print('4-Mostrar quantidade de veículos')
    print('5-Mostrar valor arrecadado')
    print('6-Encerrar programa\n')
    p = int(input('Escolha uma opção: '))

    if p == 1:
        motos += 1
        total+=5
    elif p == 2:
        carros += 1
        total+=10
    elif p == 3:
        caminhonete += 1
        total+=15
    elif p == 4:
        veiculos= motos + carros + caminhonete
        print(f'O total de veíclos é {veiculos}')
    elif p == 5:
        print(f'O valor total arrecadado é de {total}')
    elif p == 6:
        print('Encerrando programa')
        i=0
    else:
        print('Opção invalida!')
        break