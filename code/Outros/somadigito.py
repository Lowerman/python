numero = int(input("Digite o número a ser separado: "))
soma = 0
while numero > 0:
    n1 = numero % 10
    numero = numero // 10
    soma = soma + n1

print(soma)
    
