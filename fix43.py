peso = float(input("Digite seu peso: "))
sexo = input("Digite seu sexo (M/F): ").upper()
altura = float(input("Digite sua altura: "))
imc = peso / altura ** 2

if sexo == "M":
    if imc < 20.7:
        print(f"Você está abaixo do peso ideal. Seu IMC é ", imc)
    elif imc >= 20.7 and imc < 26.4:
        print(f"Você está no peso ideal. Seu IMC é ", imc)
    else:
        print(f"Você está acima do peso ideal. Seu IMC é ", imc)
else:
    if imc < 19.1:
        print(f"Você está abaixo do peso ideal. Seu IMC é ", imc)
    elif imc >= 19.1 and imc < 25.8:
        print(f"Você está no peso ideal. Seu IMC é ", imc)
    else:
        print(f"Você está acima do peso ideal. Seu IMC é ", imc)


print("Esse codigo foi desenvolvido por Guilherme Brito Pinheiro. RA: N8680D9, Turma: CC12P2")