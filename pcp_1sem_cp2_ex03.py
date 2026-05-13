# Cálculo de notas

cp1 = float(input("Digite sua nota da CP 1:\n R:"))
cp2 = float(input("Digite sua nota da CP 2:\n R:"))
cp3 = float(input("Digite sua nota da CP 3:\n R:"))

sprint1 = float(input("Digite sua nota da Sprint 1:\n R:"))
sprint2 = float(input("Digite sua nota da Sprint 2:\n R:"))
gs = float(input("Digite sua nota da Global Solution:\n R:"))

recebe_notas_cp = [cp1, cp2, cp3]

#recebe_notas_cp.remove(min(recebe_notas_cp))
#removendo menor nota das cps

if recebe_notas_cp[0] < recebe_notas_cp[1] and recebe_notas_cp[2]:
    i = recebe_notas_cp[0]
    recebe_notas_cp.remove(i)
elif recebe_notas_cp[1] < recebe_notas_cp[0] and recebe_notas_cp[2]:
    i = recebe_notas_cp[1]
    recebe_notas_cp.remove(i)
else:
    i = recebe_notas_cp[2]
    recebe_notas_cp.remove(i)

recebe_notas = recebe_notas_cp + [sprint1, sprint2]

print(recebe_notas)

media_sem1 = (sum(recebe_notas) / 4) * 0.4 + gs * 0.6

print(f"Sua média do semestre foi: {media_sem1:.1f}")

print(f"Sua média com peso foi: {media_sem1 * 0.4:.1f}")