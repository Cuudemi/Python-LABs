import ctypes
# загрузка библиотеки в ctypes #
lib = ctypes.CDLL('./lib.so')
lib.calculate_primes.restype = c.types.c_int
lib.calculate_primes.argtypes = [c.types.c_int]
D = 0  # количество делителей
x = 0
y = 0
i, j, k = 0  # для вычисления и работы с делителями

# N и M - значения промежутка NM
print('Введите 2 чётных числа: ')
N = input()
M = int(input())

primes = []
# заполняем массив #
for i in range(M):
    primes.append(1)

primes[0] = 0
primes[1] = 0

primes = libs.calculate_primes(primes, M)

for i in range(N, M, 2):
    # проверяем, можно ли разложить четное число на сумму двух простых #
    # проверим, что j - простое число, и i-j - тоже простое число #
    for j in range(2, j * 2 <= i):
        if (primes[j] == 1) and (primes[i - j] == 1):
            D = D + 1 # если оба делителя i и i-j = простые числа, то к количеству делителей прибавляем 1#
            # берем первое возможное разложение числа на 2 простых #
            if x == 0:
                x = j
                y = i - j
    print("%d %d %d %d", i, D, x, y)
    D, x, y = 0 # обнуляем значения для работы со следующим числом #