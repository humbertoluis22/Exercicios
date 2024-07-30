salarios = []
cont_abono = 100
cont = 0
cont_500 = 0
maior = 0

print("Projeção de Gastos com Abono")
print("============================ ")

while True:
    salario = input(
        "Digite o seu salario  coloque" + " ponto no lugar da virgula [0 - encerra]: "
    )

    if not salario.isnumeric():
        continue
    elif salario == "0":
        break
    salarios.append(float(salario))
    cont += 1

    salario = float(salario)
    if salario <= 500:
        cont_500 += 1
    if salario > maior:
        maior = salario

print()
for salario in salarios:
    print(f"Salário : {salario}")


print("\nSalário    - Abono")
for salario in salarios:
    if salario > 500:
        print(f"R$ {salario:<10} - R$ {salario * 0.2}")
        cont_abono += salario * 0.2
    else:
        print(f"R$ {salario:<10} - R$ 100")
        cont_abono += 100

print()
print(f"Foram processados {cont} colaboradores")
print(f"Total gasto com abonos: R$ {cont_abono:.2f}")
print(f"Valor mínimo pago a {cont_500} colaboradores")
print(f"Maior valor de abono pago: R$ {maior* 0.2:.2f}")
