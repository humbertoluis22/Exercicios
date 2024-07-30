from array import * 
import random 

teste1 = array('i',[random.randint(0,10) for i in range(10)])

for numero in teste1:
    print(numero)

teste1.reverse()
print('****************************************')
for numero in teste1:
    print(numero)