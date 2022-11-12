import log
from colors import wrap

log.title("Exercício 33")

log.statement("""
    Altere o algoritmo anterior (Fix32) para que o usuário entre com a nota do exame.
    Lembre-se que deve se realizar a média aritmética entre a média e a nota do exame.
    O sistema deverá informar a ele as seguintes mensagens:
    a) Se a média for maior ou igual a cinco: Parabéns, você aproveitou a sua chance! Está aprovado.
    b) Se a média for menor que cinco: Estude mais para a próxima. Você não alcançou o mínimo necessário.
""")

name = input("Digite seu nome: ")
ra = input("Digite seu RA: ")
grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))
exam = float(input("Digite a nota do exame: "))
average = (grade1 + grade2) / 2
final_average = (average + exam) / 2

if final_average >= 5:
    log.result(wrap("green", "Parabéns, você aproveitou a sua chance! Está aprovado."))
else:
    log.result(wrap("red", "Estude mais para a próxima. Você não alcançou o mínimo necessário."))

log.author()
