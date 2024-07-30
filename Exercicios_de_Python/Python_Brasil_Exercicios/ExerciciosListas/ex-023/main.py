usuario_byte = [
['alexandre' ,456123789],
['anderson ' ,1245698456],
['antonio  ' ,123456456],
['carlos   ' ,91257581],
['cesar    ' ,987458],
['rosemary ' ,789456125]
]
soma_mb = 0 
cont = 1

print('ACME Inc.               Uso do espaço em disco pelos usuários')
print('------------------------------------------------------------------------')
print('Nr.  Usuário        Espaço utilizado     % do uso')
for _, byte in usuario_byte:
    mb = byte / (1024 * 1024)
    soma_mb += mb

for usuario,byte in usuario_byte:
    print(f'{cont}  {usuario:<16} {(byte / (1024 * 1024)):.2f} {'MB':<16}'  + 
          f'{((byte / (1024 * 1024) / soma_mb)*100):.2f}%')
    cont+=1

print()
print(f'Espaço total ocupado: {soma_mb:.2f} MB')
print(f'Espaço médio ocupado: {(soma_mb/len(usuario_byte)):.2f} MB')