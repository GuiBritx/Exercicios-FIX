import log
from colors import wrap

log.title("Exercício 39")

log.statement("""
    O  usuário  deve  digitar  seu  nome  e  sua  idade.  O  sistema  deverá  informar  as  seguintes mensagens:
    Bem vindo NOME você é maior de idade.
    Bem vindo NOME você é menor de idade.
    Bem vindo NOME vocêé maior de 65 anos.
""")

name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))

if age >= 18:
    if age >= 65:
        log.result(wrap("green", f"Bem vindo {name} você é maior de 65 anos."))
    else:
        log.result(wrap("green", f"Bem vindo {name} você é maior de idade."))
else:
    log.result(wrap("green", f"Bem vindo {name} você é menor de idade."))

log.author()
