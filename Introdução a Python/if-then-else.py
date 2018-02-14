# -- coding: utf-8 --
# Criando um if-then-else em python

# Pedindo o input do usuário e convertendo-o para um número inteiro
numero = int(input('Insira um número inteiro: '))

# Avaliando se o número inserido é par ou ímpar
if (numero % 2 == 0):
    print ("O número %d é um número par" % numero)
else:
    print ("O número %d é um número ímpar" % numero)
