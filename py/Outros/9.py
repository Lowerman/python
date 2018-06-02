numero = int(input("Digite o número a ser separado: "))

while numero > 0:
    n1 = numero % 10
    numero = numero // 10
    print("O número separado é:", n1)
    
