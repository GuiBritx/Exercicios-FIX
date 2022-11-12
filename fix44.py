nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
media = (nota1 * 4 + nota2 * 6) / 10

print()
if media >= 9 <= 10:
    print(nome, f" você foi aprovado com conceito " 'A')
elif media >= 7:
    print(nome, f"você foi aprovado com conceito " 'B')
elif media >= 3:
    print(nome, f"você está de exame com conceito " 'C')
elif media >= 0:
    print(nome, f"você foi reprovado com conceito " 'D')


print("Esse codigo foi desenvolvido por Guilherme Brito Pinheiro. RA: N8680D9, Turma: CC12P2")