import log
from colors import wrap

log.title("Exercício 31")

log.statement("""
    Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
    (1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;
    (2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número;
    (3) se for os valores 6, 7 e 8, mostre o valor dividido 9.
""")

read_value = int(input("Digite um valor: "))
if read_value == 1 or read_value == 2 or read_value == 3:
    log.result(wrap("green", read_value ** 2))
elif read_value == 4 or read_value == 9:
    log.result(wrap("green", read_value ** (1/2)))
elif read_value == 6 or read_value == 7 or read_value == 8:
    log.result(wrap("green", read_value / 9))
else:
    log.result(wrap("red", "Valor inválido!"))

log.author()
