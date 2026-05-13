# Progrma que calcula a carga do caminhao convertido em quilos
# Calcula o preço da carga do caminhão, de acordo com o código da carga
# Calcula o imposto cobrado, de acordo com o estado de destino da carga
# Calcula o total a ser pago, somando o preço da carga e o imposto sobrado.

num_estado = int(input("Escreva um valor inteiro de 1 a 5:\n R:"))

caminhao_carga = int(input("Digite a carga do caminhão em toneladas:\n R:"))

codigo_carga = int(input("Digite o código da carga, entre 10 e 40:\n R:"))

carga_kg = caminhao_carga * 1000

if codigo_carga >= 10 and codigo_carga <= 20:
    preco_carga = carga_kg * 100
elif codigo_carga >= 21 and codigo_carga <= 30:
    preco_carga = carga_kg * 250
elif codigo_carga >= 31 and codigo_carga <= 40:
    preco_carga = carga_kg * 340
else:    
    print("Número de carga inválido. O código deve estar entre 10 e 40.")

if num_estado == 1:
    imposto_carga = ((preco_carga * 35) / 100)
elif num_estado == 2:
    imposto_carga = ((preco_carga * 25) / 100)
elif num_estado == 3:
    imposto_carga = ((preco_carga * 15) / 100)
elif num_estado == 4:
    imposto_carga = ((preco_carga * 5) / 100)
else: 
    imposto_carga = 0

print(f"O peso da carga é igual a: {carga_kg} kg\n")

print(f"O preço da carga do caminhão é R$: {preco_carga}\n")

print(f"O valor do imposto cobrado é: R$ {imposto_carga}\n")

print(f"O valor total a ser pago é R$: {preco_carga + imposto_carga}\n")