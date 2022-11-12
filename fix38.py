import log
from colors import wrap

log.title("Exercício 38")

log.statement("""
    Elabore um programa em Python que o usuário entre com seu salário. Se o salário for menor  ou  igual  a  R$1500,00  coloque  um  acréscimo  de  20%  de  aumento.
    Se  for  maior  que R$1500,00 e menor que R$2500,00 o acréscimo será de 10%, senão o acréscimo será de 5% para os demais valores.
""")

salary = float(input("Digite o salário: "))
if salary <= 1500:
    increase = 20
elif salary > 1500 and salary < 2500:
    increase = 10
else:
    increase = 5

log.result(wrap("green", f"Salário final: R$ {salary + (salary * increase / 100)}"))

log.author()
