gasolina = 2.25
carros = []
km = []

maior_km = 0
km_nome = ""

cont = 0

for i in range(1, 6):
    print(f"Veiculos {i}")
    nome = input("Nome: ")
    km_litro = float(input("Km por litro : "))
    carros.append(nome)
    km.append(km_litro)

    if km_litro > maior_km:
        maior_km = km_litro
        km_nome = nome

print("\nRelatório Final")

carros_km = zip(carros, km)
for carro, km in carros_km:
    cont += 1
    print(
        f"{cont} - {carro:<15} - {km:<5} - {(1000/km):.1f} litros - R$ {((1000/km)*gasolina):.2f} "
    )
print(f"O menor consumo é do {km_nome}.")
