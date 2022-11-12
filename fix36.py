import log
from colors import wrap

log.title("Exercício 36")

log.statement("""
    Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
    (1) se for um valor negativo, mostre o módulo (valor sem sinal) do valor;
    (2) se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles;
    (3) Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5
""")

read_value = int(input("Digite um valor: "))
if read_value < 0:
    log.result(wrap("green", abs(read_value)))
elif read_value > 10:
    read_value2 = int(input("Digite outro valor: "))
    log.result(wrap("green", read_value - read_value2))
else:
    log.result(wrap("green", read_value / 5))

log.author()