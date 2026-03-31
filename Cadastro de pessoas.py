contfem = 0
contmas = 0
contida = 0

while True:
    print("-" * 30, "CADASTRE UMA PESSOA", "-" * 30)
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
            print ("por favor, digite um número válido")
    if idade > 18:
        contida += 1

    sexo = " "
    while sexo not in "MF":
        sexo = input("Digite seu sexo (M/F): ").upper()
    if sexo == "F" and idade < 20:
        contfem += 1
    elif sexo == "M":
        contmas += 1

    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ").upper()
    if continuar == "N":
        break

print (f"O total de pessoas com mais de 18 anos: {contida}")
print (f"O total de homens cadastrados é {contmas}")
print (f"E temos {contfem} mulheres com menos de 20 anos")