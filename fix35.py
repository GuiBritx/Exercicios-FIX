import log
from colors import wrap

log.title("Exercício 35")

log.statement("""
    Elabore um programa em PYTHON, que mostre  os descontos  concedidos  pela  loja  ABC  em suas mercadorias.
    Em  compras  acima  de  R$  300,00  forneça  20\%  de  desconto, 
    entre  R$  200,00  a  R$  299,99 desconto de 10\% e abaixo de R$ 199,99 o desconto será de 5%.
    Mostre na tela o valor total e o valor final a pagar (com o desconto).
    Solicite ao usuário que digite os valores via teclado.
""")

value = float(input("Digite o valor da compra: "))
if value > 300:
    discount = 20
elif value >= 200 and value <= 299.99:
    discount = 10
else:
    discount = 5

log.result(wrap("green", f"Valor total: R$ {value}"))
log.result(wrap("green", f"Valor final: R$ {value - (value * discount / 100)}"))

log.author()
