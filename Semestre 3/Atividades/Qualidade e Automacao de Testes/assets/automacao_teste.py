def saque(valor, saldo, limite_credito):
    status = False
    if valor <= saldo:
        saldo = saldo - valor
        status = True
    elif valor <= limite_credito:
        limite_credito = limite_credito - valor
        status = True
    #return status, saldo, limite_credito
    print("Saque realizado?", status)
    print("Saldo:", saldo)
    print("Limite de crédito:", limite_credito)

print("="*21 + ' CASO 1 ' + "="*21)

print("Caso de Teste 1: Valor solicitado menor ou igual ao saldo disponível")
print("Valor Solicitado: 600, Saldo: 1000, credito: 0, Status esperado: True")
saque(600, 1000, 0)
print("-"*50)
print("Valor Solicitado: 1000, Saldo: 1000, credito: 0")
saque(1000, 1000, 0)

print("="*21 + ' CASO 2 ' + "="*21)

print("Caso de Teste 2: Valor solicitado maior do que saldo disponível, porém menor do que credito disponível, Status esperado: True")
print("Valor Solicitado: 1500, Saldo: 1000, credito: 2000")
saque(1500, 1000, 2000)

print("="*21 + ' CASO 3 ' + "="*21)

print("Caso de Teste 3: Valor solicitado ultrapassa saldo e credito disponiveis, Status esperado: False")
print("Valor Solicitado: 1500, Saldo: 500, credito: 250")
saque(1500, 500, 250)