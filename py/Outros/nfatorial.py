numero = int(input("Digite o valor de n: "))
var = numero
    
if numero > 0:
    while var > 2:
        #fatorial = numero * (numero-1) * (numero-2) * (numero-3) * (numero -4)
        var = var - 1
        numero = numero * var
else : numero = 1

print(numero)
    
