# Programa que leia 4 valores que representam os lados de um triângulo A, B e C.

lado_a = int(input("Digite o valor do lado A do triângulo:\n R:"))
lado_b = int(input("Digite o valor do lado B do triângulo:\n R:"))
lado_c = int(input("Digite o valor do lado C do triângulo:\n R:"))

recebe_lados = [lado_a, lado_b, lado_c]

recebe_lados.sort(reverse=True)

print(recebe_lados)
if recebe_lados[0] >= recebe_lados[1] + recebe_lados[2]:
    print("NAO FORMA TRIANGULO")

if recebe_lados[0] **2 == recebe_lados[1] **2 + recebe_lados[2] **2:
    print("TRIANGULO RETANGULO")

if recebe_lados[0] **2 > recebe_lados[1] **2 + recebe_lados[2] **2:
    print("TRIANGULO OBTUSANGULO")

if recebe_lados[0]**2 < recebe_lados[1]**2 + recebe_lados[2] **2:
    print("Triangulo ACUTANGULO")

if recebe_lados[0] == recebe_lados[1] and recebe_lados[0] == recebe_lados[2]:
    print("TRIANGULO EQUILATERO")

elif recebe_lados[0] == recebe_lados[1] or recebe_lados[0] == recebe_lados[2] or recebe_lados[1] == recebe_lados[2]:
    print("TRIANGULO ISOSCELES")
