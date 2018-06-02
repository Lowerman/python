def  fatorial(numero):
    var = numero
    if numero > 0:
        while var > 2:
            var = var - 1
            numero = numero * var
    else : numero = 1
    return(numero)

def coeficiente(n,k):
    return fatorial(n)/(fatorial(k)*fatorial(n-k))

    
