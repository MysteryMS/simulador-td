def ler_tipo():
    response = input(
        "Qual tipo de investimento você quer simular?\n\n[1] Tesouro Pré Fixado 2024\n[2] Tesouro Pré Fixado 2026\n\n> ")
    if response == "1":
        return 1
    elif response == "2":
        return 2
    else:
        print("Opção inválida, tente novamente.")
        return ler_tipo()

def ler_valor():
    response = input("Qual o valor inicial do investimento?\n> ")
    try:
        if float(response) < 30:
            print("O valor mínimo é de 30 reais.")
            return ler_valor()
        return float(response)
    except ValueError:
        print("Valor inválido, tente novamente.")
        return ler_valor()

def ler_aporte():
    response = input("Qual o valor do aporte mensal?\n> ")
    try:
        if float(response) <= 0:
            print("Insira um valor.")
            return ler_aporte()
        return float(response)
    except ValueError:
        print("Valor inválido, tente novamente.")
        return ler_aporte()

def ler_resposta():
    response = input("Deseja realizar outra simulação?\n[1] Sim\n[2] Não\n> ")
    if response == "1":
        return 1
    elif response == "2":
        return 2
    else:
        print("Opção inválida, tente novamente.")
        return ler_resposta()


while True:
    print("--------------------------------")
    print("Bem vindo ao simulador de\ninvestimentos do Tesouro Direto.")
    print("--------------------------------")
    tipo = ler_tipo()

    liquido = None
    imposto = None
    b3 = None

    if tipo == 1:
        print("\n\nSimulando investimento no Tesouro Pré Fixado 2024.\n")
        valor_inicial = ler_valor()
        aporte = ler_aporte()
        juros = 12.26
        montante = valor_inicial
        meses = 32

        montante = (aporte * meses) + valor_inicial
        total_juros = montante * (juros / 100)
        bruto = montante + total_juros

        imposto = (bruto - montante) * (15 / 100)
        b3 = bruto * (2.5 / 100 / meses)

        liquido = bruto - imposto - b3
    
    elif tipo == 2:
        print("\n\nSimulando investimento no Tesouro Pré Fixado 2026.\n")
        valor_inicial = ler_valor()
        aporte = ler_aporte()
        juros = 12.18
        montante = valor_inicial
        meses = 50

        montante = (aporte * meses) + valor_inicial
        total_juros = montante * (juros / 100)
        bruto = montante + total_juros

        imposto = (bruto - montante) * (15 / 100)
        b3 = bruto * (2.5/ 100 / meses)

        liquido = bruto - imposto - b3
        
    
    print("-----------------------------------")
    print("      Resultado da Simulação       ")
    print("-----------------------------------")
    print("Valor inicial            R$ {:.2f}".format(valor_inicial))
    print("Aporte mensal            R$ {:.2f}".format(aporte))
    print("Aportes mensais          {}".format(meses))
    print("Juros                    R$ {:.2f}%".format(juros))
    print("Taxa B3                  R$ {:.2f}".format(b3))
    print("Taxa do Imposto de Renda R$ {:.2f}".format(imposto))
    print("Valor investido          R$ {:.2f}".format(montante))
    print("Valor bruto              R$ {:.2f}".format(bruto))
    print("Liquido                  R$ {:.2f}".format(liquido))
    print("-----------------------------------")

    prompt = ler_resposta()
    if prompt == 2:
        print("Obrigado por utilizar nosso simulador.")
        break
    else:
        print("\n" * 100)
  