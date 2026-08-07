''' O NumPy (Numerical Python) é a biblioteca base do Python para computação numérica e científica. Ele serve para criar e manipular arrays e matrizes multidimensionais de forma extremamente rápida e eficiente '''
import teste_numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([(10, 20, 30), (100, 200, 300)])
print(b)

''' Cria uma matriz '''
c = np.ones((7, 5))
print(c)

d = np.eye(8)
print(d)