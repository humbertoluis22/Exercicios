numeros_1 =[1,2,3,4,5,6,7,8,9,10]
numeros_2 = [11,12,13,14,15,16,17,18,19,20]
numeros_3 = []

for i in range(0,10):
    numeros_3.append(numeros_1[i])
    numeros_3.append(numeros_2[i])

print(f'Numeros 1 : {numeros_1} ')
print(f'Numeros 2 : {numeros_2} ')
print(f'Numeros intercalados : {numeros_3} ')