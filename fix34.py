import log
from colors import wrap

def fact(x): return 1 if x == 0 else x * fact(x - 1)

log.title("Exercício 34")

log.statement("""
    Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
    (1) se o valor for 1 e 2, mostre o valor elevado ao cubo;
    (2) se o valor for múltiplo de 3 mostre o fatorial desse número;
    (3) se o valor for os valores 4, 5, 7 ou 8, mostre o valor dividido 9. Caso não se ja nenhum dos valores, informe como “valor inválido”.
""")

read_value = int(input("Digite um valor: "))

if read_value == 1 or read_value == 2:
    log.result(wrap("green", read_value ** 3))
elif read_value % 3 == 0:
    log.result(wrap("green", fact(read_value)))
elif read_value == 4 or read_value == 5 or read_value == 7 or read_value == 8:
    log.result(wrap("green", read_value / 9))
else:
    log.result(wrap("red", "Valor inválido!"))

log.author()