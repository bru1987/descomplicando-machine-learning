# -*- coding: utf-8 -*-

# Definindo numpy
import numpy as np

# Criando uma matriz
a = np.random.random_integers(0, 4, (3, 3))
print ("Matriz A\n", a)
b = np.random.random_integers(0, 4, (3, 3))
print ("Matriz B\n" ,b)

# Tomando as dimensões de uma matriz
print ("A matriz A tem a forma", a.shape)
print ("A matriz A tem a forma", b.shape)

# Fazendo cálculos simples (soma, subtração, multiplicação e divisão)
# Soma de matrizes
print("Matriz A+B\n", np.add(a,b))
# Subtração de matrizes
print("Matriz A-B\n", np.subtract(a,b))
# Multiplicação de matrizes
print("Matriz A*B elementwise\n", np.dot(a,b))
# Multiplicação elementwise
print("Matriz A*B\n", np.multiply(a,b))
# Criando uma matriz identidade
print("Matriz Identidade\n", np.identity(3))
# Criando uma matriz de um's
print("Matriz com 1's\n", np.ones((3,3)))
