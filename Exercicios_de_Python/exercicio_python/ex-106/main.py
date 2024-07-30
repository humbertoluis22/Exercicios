numeros1 = [1,2,3] 
numeros2 = [4,5,6]
numeros3 =[]

for numero in numeros1:
    for numero2 in numeros2:
        if numero != numero2: 
                numeros3.append((numero,numero2))

print(numeros3)