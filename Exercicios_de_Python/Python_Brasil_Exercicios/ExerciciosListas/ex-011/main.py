numeros_1 =[1,2,3,4,5,6,7,8,9,10]
numeros_2 = [11,12,13,14,15,16,17,18,19,20]
numeros_3 = [30,31,32,33,34,35,36,37,38,39]
numeros_4 = []

for i in range(0,10):
    numeros_4.append(numeros_1[i])
    numeros_4.append(numeros_2[i])
    numeros_4.append(numeros_3[i])

print(numeros_4)
print(f'Numeros 1 : {numeros_1} ')
print(f'Numeros 2 : {numeros_2} ')
print(f'Numeros 3 : {numeros_3} ')
print(f'Numeros intercalados : {numeros_4} ')