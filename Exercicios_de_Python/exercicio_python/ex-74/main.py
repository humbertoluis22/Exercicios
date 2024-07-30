palavra_contraria = ''
palavra = 'Bem vindo ao mundo da programação!!!'

for i in range(len(palavra) + 1):
    if i == 0: 
        continue
    palavra_contraria +=  palavra[-i]

print(palavra)
print()
print(palavra_contraria)