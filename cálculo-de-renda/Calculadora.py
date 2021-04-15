import sys
print('Boas vindas à calculadora de salário!')
print('Aqui vamos poder observar o quanto você ganha por hora, o quanto ganha no final do mês e o quanto' 
' você ganha por dia.')
print('Se você quiser saber o quanto ganha por hora, digite (1). Já se quer saber o quanto ganha por dia, digite (2).'
' Já se quer saber o quanto ganhará no final do mês, digite (3).')
opção = input('Digite sua opção (1) (2) ou (3): ')
if len(opção) > 1 or len(opção) < 1:
    print('Verifique se você digitou corretamente!')
    sys.exit()
if not opção.isnumeric():
    print('Verifique se você digitou corretamente!')
    sys.exit()
if opção == '1':
    print('Você escolheu ver o quanto ganha por hora!')
    print('Para isso, preciso de algumas informações...')
    salário = input('Quanto você ganha no final do mês?: ')
    horas = input('Quantas horas você trabalha por dia?: ')
    mês = input('Quantos dias tem o mês que você está calculando?: ')
    try:
        salário = float(salário)
        horas = float(horas)
        mês = int(mês)
    except:
        print('ERRO! Verifique se você digitou os números de forma correta!')
    if horas > 24 or horas < 0:
        print('ERRO! Verifique se você digitou corretamente!')
        sys.exit()
    elif mês > 31 or mês < 0:
        print('ERRO, Verifique se você digitou os valores corretamente!')
        sys.exit()
    horas_trabalhadas = mês * horas
    print(f'Durante esse mês, você trabalhou {horas_trabalhadas} horas!')
    ganhoporhora = salário / horas_trabalhadas
    print(f'Com isso, podemos concluir que o seu ganho por hora é de R$ {ganhoporhora:.2f}')
if opção == '2':
    print('Você escolher ver o quanto ganha por dia!')
    print('Para isso, preciso de algumas informações...')
    salário = input('Por favor, informe seu salário: ')
    mês = input('Quantos dias tem o mês que você trabalhou?: ')
    try:
        salário = float(salário)
        mês = int(mês)
    except:
        print('ERRO! Verifique se você digitou os valores corretos!')
    if mês > 31 or mês < 0:
        print('ERRO! Verifique se você digitou corretamente as informações!')
        sys.exit()
    ganhopordia = salário/mês
    print(f'O seu ganho por dia é de R${ganhopordia:.2f}')
if opção == '3':
    print('Você escolheu saber o quanto ganhará no final do mês!')
    print('Para isso, preciso de algumas informações...')
    ganhopordia = input('Quanto você ganha por dia?: ')
    mês = input('Quantos dias tem o mês que você trabalhou?: ')
    try:
        ganhopordia = float(ganhopordia)
        mês = int(mês)
    except:
        print('ERRO! Verifique se os valores estão digitados corretamente!')
        sys.exit()
    if mês > 31 or mês < 0:
        print('ERRO! Verifique se você digitou seus valores corretamente!')
    ganhopormês = ganhopordia * mês
    print(f'O seu ganho no final do mês será de R${ganhopormês:.2f}')
    print('')
    print('Agora vamos poder ver o quanto de impostos você precisa pagar e qual o seu salário líquido...')
    print('Vale lembrar, que quem recebe mais do que R$ 1903.00 mensalmente, necessita pagar imposto de renda!')
    if ganhopormês < 1903:
        print('Você não precisa pagar imposto de renda!')
        sys.exit()
    elif ganhopormês > 1903 and ganhopormês < 2826:
        print('Na sua renda, é necessário pagar "7.5%" de imposto de renda!')
        imposto = (7.5 * ganhopormês) / 100
        impostosobrado = ganhopormês - imposto
        print(f'Na sua renda, é necessário pagar R${imposto:.2f} para o imposto de renda!')
        print(f'Após esse pagamento, te sobram R${impostosobrado:.2f}')
    elif ganhopormês > 2826 and ganhopormês < 3751:
        print('Na sua renda, é necessário pagar "15%" de imposto de renda!')
        imposto = (15 * ganhopormês) / 100
        impostosobrado = ganhopormês - imposto
        print(f'Na sua renda, é necessário pagar R${imposto:.2f} para o imposto de renda!')
        print(f'Após esse pagamento, te sobram R${impostosobrado:.2f}')
    elif ganhopormês > 3751 and ganhopormês < 4664:
        print('Na sua renda, é necessário pagar "22.5%" de imposto de renda!')
        imposto = (22.5 * ganhopormês) / 100
        impostosobrado = ganhopormês - imposto
        print(f'Na sua renda, é necessário pagar R${imposto:.2f} para o imposto de renda!')
        print(f'Após esse pagamento, te sobram R${impostosobrado:.2f}')
    elif ganhopormês > 4664:
        print('Na sua renda, é necessário pagar "27.5%" de imposto de renda!')
        imposto = (27.5 * ganhopormês) / 100
        impostosobrado = ganhopormês - imposto
        print(f'Na sua renda, é necessário pagar R${imposto:.2f} para o imposto de renda!')
        print(f'Após esse pagamento, te sobram R${impostosobrado:.2f}')
    print('')
    print('Seu salário também precisa ir para o pagamento do INSS.')
    salárioimposto = impostosobrado
    if salárioimposto <= 1045:
        print('Você precisa contribuir com "7.5%" do seu salário')
        inss = (7.5 * salárioimposto) / 100
        print(f'A sua contribuição para o INSS será de R$ {inss:.2f}')
        salárioinss = salárioimposto - inss
        print(f'Com isso te sobram R${salárioinss:.2f}')
    elif salárioimposto < 2089:
        print('Você precisa contribuir com "9%" do seu salário')
        inss = (9 * salárioimposto) / 100
        print(f'A sua contribuição para o INSS será de R$ {inss:.2f}')
        salárioinss = salárioimposto - inss
        print(f'Com isso te sobram R${salárioinss:.2f}')
    elif salárioimposto < 3134:
        print('Você precisa contribuir com "12%" do seu salário')
        inss = (12 * salárioimposto) / 100
        print(f'A sua contribuição para o INSS será de R$ {inss:.2f}')
        salárioinss = salárioimposto - inss
        print(f'Com isso te sobram R${salárioinss:.2f}')
    elif salárioimposto < 6101:
        print('Você precisa contribuir com "14%" do seu salário')
        inss = (14 * salárioimposto) / 100
        print(f'A sua contribuição para o INSS será de R$ {inss:.2f}')
        salárioinss = salárioimposto - inss
        print(f'Com isso te sobram R${salárioinss:.2f}')
    salárioliquido = salárioinss
    print(f'Com isso, o seu salário líquido fica cerca de R$ {salárioliquido:.2f}')  