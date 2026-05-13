#Calculo de salario de funcionario.

nome_func = input("Digite o nome do funcionário:\n R:")
cargo_func = input("Digite o cargo do funcionário:\n 1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário\n R:")
salario_func = float(input("Digite o salário do funcionário:\n R:"))
horas_extras_func = int(input("Digite a quantidade de horas extras trabalhadas:\n R:"))
total_faltas_func = int(input("Digite a quantidade de faltas do funcionário:\n R:"))
bonus_func = input("Recbeu bônus? (S/N)\n R:")

# Padrão 220 horas mensais, 8 horas diárias, 44 semanais, 4 semanas por mês.

def calcular_horas_extras(horas_extras_func, salario_func):
    valor_hora_extra = horas_extras_func * (salario_func / 220) * 1.5
    return valor_hora_extra

valor_horas_extras = calcular_horas_extras(horas_extras_func, salario_func)


def calcular_bonus_salario(cargo_func, bonus_func):
    if bonus_func == "S" or bonus_func == "s" or bonus_func == "Sim" or bonus_func == "sim":
        if cargo_func == "1":
            bonus_salario = 1000
        if cargo_func == "2":
            bonus_salario = 500
        if cargo_func == "3":
            bonus_salario = 300
        if cargo_func == "4":
            bonus_salario = 100
    
    return bonus_salario

bonus_salario = calcular_bonus_salario(cargo_func, bonus_func)

def calcular_desconto_faltas(total_faltas_func, salario_func):
    valor_desconto_faltas = salario_func * (total_faltas_func * 0.02)
    return valor_desconto_faltas

valor_desconto_faltas = calcular_desconto_faltas(total_faltas_func, salario_func)

print(f"Funcionário: {nome_func}")

print(f"Salário Bruto: R$ {salario_func}")

print(f"Total de acréscimos por horas extras + bonus: R$: {valor_horas_extras + bonus_salario}")

print(f"Total de descontos por faltas: R$ {valor_desconto_faltas:.2f}")

print(f"Salário Líquido do {nome_func}: R$ {salario_func + valor_horas_extras + bonus_salario - valor_desconto_faltas}")


