# -*- coding: utf-8 -*-
# Criando um programa com um while loop

potencia = 10
numero = 0

while potencia != 0:
    numero = 2**(10-potencia+1)
    print ("O número 2 elevado a %d é igual a %f" % ((10-potencia+1),numero))
    potencia -= 1

print ("Acabou!")
