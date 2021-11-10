cpf = codigo = pedidoMaisCaro = valorDaCompra = valor = valorMotoboy = valorProprietário = 0
pedidoMaisBarato = 99999999999999999999999999


while cpf != -1:
    print(6 * '-=')
    print('EGGS Lanches')
    print(6 * '-=', '\n')
    cpf = int(input('Digigte o cpf do cliente: '))
    if cpf == -1:
        break
    valorDaCompra = valorDaCompra - valorDaCompra
    while codigo != -1:
        print('''Cardápio:
           PRODUTO******CÓDIGO******VALOR
        Cachorro Quente--100------R$ 4,20
        Bauru Simples----101------R$ 7,30
        Bauru com ovo----102------R$ 8,50
        Hambúrguer-------103------R$ 9,20
        Cheeseburguer----104------R$ 10,30
        Refrigerante-----105------R$ 8,00
        ''')
        codigo = int(input('Digite o código do produto escolhido: '))
        if codigo == -1:
            break

        qte = int(input('Qual a quantidade desse produto desejada? '))
        if codigo == 100:
            valor = 4.20 * qte
        elif codigo == 101:
            valor = 7.30 * qte
        elif codigo == 102:
            valor = 8.50 * qte
        elif codigo == 103:
            valor = 9.20 * qte
        elif codigo == 104:
            valor = 10.30 * qte
        elif codigo == 105:
            valor = 8 * qte
        valorDaCompra = valorDaCompra + valor
    frete = int(input('Qual o valor do frete de acordo com a localidade do cliente? '))
    valorMotoboy = valorMotoboy + (frete * 0.6)
    if codigo == -1:
        codigo = codigo + 1
    print(f'O valor total dessa compra foi de: R${valorDaCompra + frete:.2f}')
    valorProprietário = valorProprietário + (valorDaCompra +(frete * 0.4))
    if (valorDaCompra + frete) > pedidoMaisCaro:
        pedidoMaisCaro = (valorDaCompra + frete)
    if (valorDaCompra + frete) < pedidoMaisBarato:
        pedidoMaisBarato = (valorDaCompra + frete)
print(f'O valor mais caro do expediente foi: R${pedidoMaisCaro}')
print(f'O valor pago pelo cliente com o pedido mais barato do expediente foi: R${pedidoMaisBarato}')
print(f'O valor arrecadado pelo motoboy no final do expediente foi de: R${valorMotoboy}')
print(f'O valor total arrecadado pelo proprietário do EGGS Lanches no final do expediente foi de: R${valorProprietário}')
