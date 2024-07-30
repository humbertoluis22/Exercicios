print("********** calculadora **********\n")
numero1 = int(input('digite o primeiro numero : '))
numero2 = int(input('digite o segundo numero :'))

sum = lambda x,y: x+ y
sub = lambda x,y : x - y 
div = lambda x,y : x / y 
mult = lambda x,y : x * y 

print("\n********** escolha uma opção **********\n")
opcao = input("""
1 - soma
2 - subtracao 
3 - divisao
4 - multiplicacao

escolha [1 | 2 | 3 | 4] :"""
)
 
if not opcao.isnumeric():
    print('opção invalida')

elif opcao == '1':
    print(sum(numero1,numero2))
elif opcao == '2':
    print(sub(numero1,numero2))
elif opcao =='3':
    print(div(numero1,numero2))
elif opcao == '4':
    print(mult(numero1,numero2))