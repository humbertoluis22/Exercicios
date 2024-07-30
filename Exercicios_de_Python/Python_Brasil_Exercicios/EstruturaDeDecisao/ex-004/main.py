letra:str = input('Digite uma letra: ').upper().strip()

if not letra.isalpha():
    print('Digite apenas letras')
elif len(letra) > 1 :
    print('Digite apenas uma letra!! ')
elif letra in ('AEIOU'):
    print('Você digitou uma vogal !!')
else:
    print('Você digitou uma consoante !!')
