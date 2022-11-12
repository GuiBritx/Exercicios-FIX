


name = input("Digite seu nome: ")
salary = float(input("Digite seu salário: "))
if salary <= 1500:
    increase = 20
elif salary > 1500 and salary < 2500:
    increase = 10
else:
    increase = 5

print( f"Salário final: R$ {salary + (salary * increase / 100)}")
print("Esse codigo foi desenvolvido por Guilherme Brito Pinheiro. RA: N8680D9, Turma: CC12P2")
