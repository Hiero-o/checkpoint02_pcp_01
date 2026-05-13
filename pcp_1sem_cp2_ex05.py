nome_cliente = input("Digite o nome do cliente:\nR: ")
idade_cliente = int(input("Digite a idade do cliente:\nR: "))
renda_cliente = float(input("Digite a renda mensal do cliente:\nR: "))
valor_financ = float(input("Digite o valor do financiamento:\nR: "))
num_parcelas = int(input("Digite o número de parcelas desejado (3 até 24):\nR: "))


def pode_aprovar(idade_cliente, renda_cliente, valor_financ):
    if idade_cliente >= 18 and valor_financ <= (renda_cliente * 20):
        return True
    else:
        return False


if num_parcelas < 3 or num_parcelas > 24:
    print("Número de parcelas inválido.")
    exit()


if pode_aprovar(idade_cliente, renda_cliente, valor_financ) == False:
    print("Financiamento negado.")
    exit()


def calcular_taxa_juros(num_parcelas):
    if num_parcelas <= 6:
        taxa_juros = 0.06
    elif num_parcelas <= 12:
        taxa_juros = 0.08
    else:
        taxa_juros = 0.10
    return taxa_juros

tot_taxa_juros = calcular_taxa_juros(num_parcelas)


def calcular_valor_parcela(valor_financ, taxa_juros, num_parcelas):

    valor_parcela = (
        valor_financ *
        (taxa_juros * (1 + taxa_juros) ** num_parcelas)) / (((1 + taxa_juros) ** num_parcelas) - 1)
    return valor_parcela

tot_valor_parcela = calcular_valor_parcela(valor_financ, tot_taxa_juros, num_parcelas)


def calcular_total(valor_parcela, num_parcelas):
    total_pago = valor_parcela * num_parcelas
    return total_pago

tot_total_pago = calcular_total(tot_valor_parcela, num_parcelas)


def calcular_total_juros(total_pago, valor_financ):
    total_juros = total_pago - valor_financ
    return total_juros


tot_total_juros = calcular_total_juros(tot_total_pago, valor_financ)


print("\n===== RESULTADO =====\n")

print(f"Cliente: {nome_cliente}")

print(f"Valor do financiamento: R$ {valor_financ}")

print(f"Quantidade de parcelas: {num_parcelas}")

print(f"Taxa de juros aplicada: {tot_taxa_juros * 100}%")

print(f"Valor da parcela: R$ {tot_valor_parcela:.2f}")

print(f"Total a ser pago: R$ {tot_total_pago:.2f}")

print(f"Total de juros pago: R$ {tot_total_juros:.2f}")