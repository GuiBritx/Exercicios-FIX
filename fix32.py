import log
from colors import wrap

log.title("Exercício 32")

log.statement("""
    Faça um algoritmo que calcule a média do aluno. Ele deve entrar com seu nome, RA, nota 1 e nota 2.
    O sistema deverá informar a ele as seguintes mensagens:
    a) Se a média for maior ou igual a sete: Parabéns, você está aprovado!
    b) Se  a  média  for  menor  que  sete:  Você  ainda  tem  uma  chance!  Estude  mais  para  o exame.
""")

name = input("Digite seu nome: ")
ra = input("Digite seu RA: ")
grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))
average = (grade1 + grade2) / 2

if average >= 7:
    log.result(wrap("green", "Parabéns, você está aprovado!"))
else:
    log.result(wrap("red", "Você ainda tem uma chance! Estude mais para o exame."))

log.author()
