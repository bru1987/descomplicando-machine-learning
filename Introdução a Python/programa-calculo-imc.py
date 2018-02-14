# -*- coding: utf-8 -*-

peso_em_kg = 72
altura_em_metros= 1.75

IMC = round((peso_em_kg/(altura_em_metros*altura_em_metros)),2)

print ("O IMC de uma pessoa com %d kg e %f metros de altura é %f" % (peso_em_kg,altura_em_metros,IMC))

# Incluir tabela de valores, para mostrar se o IMC está normal, acima ou abaixo
