import log
from colors import wrap

log.title("Exercício 37")

log.statement("""
    Nesse programa o usuário deve entrar com um número e o sistema retornar se ele é divisível por 10 ou se é divisível por 5 ou se é divisível por 2,
    caso contrário retornar que o valor não é divisível por nenhum desses valores.
""")

read_value = int(input("Digite um valor: "))
if read_value % 10 == 0:
    log.result(wrap("green", "Divisível por 10"))
elif read_value % 5 == 0:
    log.result(wrap("green", "Divisível por 5"))
elif read_value % 2 == 0:
    log.result(wrap("green", "Divisível por 2"))
else:
    log.result(wrap("red", "Não é divisível por nenhum desses valores"))

log.author()
