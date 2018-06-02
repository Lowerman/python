# Primeiro:

n = int(input("Digite um número inteiro: ")) 
if n % 2 == 0:    
    print("Par")
else :
    print("ímpar")

# Segundo:

if n % 3 == 0:
    print("Fizz")
else : print (n)

# Terceiro

if n % 5 == 0:
    print("Buzz")
else : print (n)

# Quarto

if n % 3 and 5 == 0:
    print("FizzBuzz")
else : print (n)

# Quinto

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: ")) 
n3 = int(input("Digite um número inteiro: "))
if n1 < n2 and n2 < n3:
    print("crescente")
else : print("não está em ordem crescente")
