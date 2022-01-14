'''
ТЗ

1. Вычисляется сумма (Е)
2. Умножаем случайный элемент матрицы на -1
3. Вычисляем E' новой системы
4. Вычислить E' - E = delta
5.1. Если delta <=0: вернуться к (2)

5.2. Иначе:
а) вычислить W = exp( -delta/T ), T=float (0; 10)
б) Выбрать случайное p=float (0;1)
в) Сравнить P v W
г) Если W >=P: вывести матрицу
д) иначе: Вернуться к (2)
'''


import numpy as np
import random
import matplotlib.pyplot as plt

T = float(input('Введите Т: '))
x = int(input('input size: '))
C_N = range(x)
matrix = np.zeros((x, x))
for i in range(x):
    for j in range(x):
        matrix[i, j] = random.choice([-1,1])
print(matrix)


mas = []
mas = matrix.copy()
for i in range(int(input('input iteration count: '))):
    E = E1 = 0
    for j in range(x):
        for k in range(x):
            E += matrix[j][k] * matrix[j][k - 1] + matrix[j - 1][k] * matrix[j][k]
            #E*=-1
    mas1 = []
    mas1 = matrix.copy()
    mas1[random.choice(C_N)][random.choice(C_N)] *= -1
    for j in range(x):
        for k in range(x):
            E1 += mas1[j][k] * mas1[j][k - 1] + mas1[j - 1][k] * mas1[j][k]
            #E1*=-1
    deltaE = -1 * (E1 - E)

    if deltaE <= 0:
        matrix = mas1.copy()
        mas = matrix.copy()
    else:
        
        P = random.random()
        W = np.exp(-deltaE/T)
        if P <= W:
            mas = matrix.copy()
        else:
            matrix = mas.copy()
    #print(matrix)
    plt.clf()
    plt.imshow(matrix)
    plt.draw()
    plt.show()
    plt.gcf().canvas.flush_events()
plt.ioff()