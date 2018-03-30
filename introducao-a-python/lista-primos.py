primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

primos_abaixo_de_25 = primos[0:8]
print(primos_abaixo_de_25)

# (a) Exibindo o número de elementos da lista
print("O número de elementos desta lista é", len(primos))

# (b) Uma só linha
print(primos[0:8])

# (c)Usando o input do usuário
maximo = int(input("Insira o valor máximo para a lista: "))
nova_lista = []

for i in primos:
    if i <= maximo:
        nova_lista.append(i) 
        
print("Números primos até", maximo,":",nova_lista)