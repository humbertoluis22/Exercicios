from array import * 

lista = array('i',[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])

print(f'tamanho da lista : {len(lista)}\n')
print(f'tamanho de bytes: {lista.itemsize}\n')
print(f'espaço alocado em memoria: {lista.buffer_info()[0]}')
