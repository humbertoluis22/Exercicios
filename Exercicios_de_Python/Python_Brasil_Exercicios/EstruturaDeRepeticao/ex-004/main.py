a = 80000
b = 200000
contador = 0

while a < b :
    crescimento_a = a * 0.03
    crescimento_b  = b * 0.015
    a += crescimento_a
    b += crescimento_b
    contador +=1

print(f'Serão necessarios {contador} anos para o pais A se igual ou passar o B')