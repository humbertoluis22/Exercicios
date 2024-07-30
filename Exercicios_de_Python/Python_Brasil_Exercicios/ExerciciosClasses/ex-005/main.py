from conta_corrente import ContaCorrente

conta_1 = ContaCorrente(1234,'humberto')
print(conta_1)
conta_1.depositar(2000)
conta_1.alterar_nome('Humberto Luis')
print(conta_1)
conta_1.saque(100)
print(conta_1)