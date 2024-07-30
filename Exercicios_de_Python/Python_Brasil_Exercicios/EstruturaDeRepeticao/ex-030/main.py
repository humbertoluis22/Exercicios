print("Informe o valor do pão !!")
valor = input("Preço do pão: ")
while not valor.replace('.','').isnumeric():
    print("Digite apenas numeros com separador '.' !!")
    valor = input("Preço do pão: ")

print("\nPanificadora Pão de Ontem - Tabela de preços\n")
for i in range(1,50+1):
    print(f"{i} - R$ {(i * float(valor)):.2f}")