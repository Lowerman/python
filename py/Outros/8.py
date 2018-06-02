tamanho = int(input("Digite o tamanho da sequênciade números: "))

print("Digite uma sequêcia de valores terminada por zero.")
soma = 0
i = 1

while i <= tamanho: 
    valor = int(input("Digite um número: "))
    soma = soma + valor
    i = i + 1

print("A soma dos valores digitados é:",soma)
    
