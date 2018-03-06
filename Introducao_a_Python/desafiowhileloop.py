# -*- coding: utf-8 -*-
# Criando um programa com um while loop

# (a)
print ("Item a")

inicio = 1
fim = 10
soma_a = 0

contador = 1
while contador <= (fim-inicio+1):
    soma_a += fim
    print("Soma = %d" % (soma_a))
    fim -= 1

# (b)
print ("Item b")

inicio = 1
fim = 10
stop = fim-inicio+1
soma_b = 0
contador = 1

while contador <= stop: # vamos contar quantos números foram somados
    if (contador % 2 == 0): # o contador é par
        soma_b += fim
        fim -= 1
        contador += 1
    else: # o contador é ímpar
        soma_b += inicio
        inicio += 1
        contador += 1
    print("Soma = %d" % (soma_b) )

print ("(a) A soma é %d" % (soma_a))
print ("(b) A soma é %d" % (soma_b))
