import csv
import statistics
import sys
import split_data


def read_data_from_file(file: str) -> list:
    """ Данная функция читает файл csv с пропуском первой строки и возвращает массив строк """
    data = []
    with open(file, 'r') as file:
        next(file)
        f = csv.reader(file, dialect="excel")
        for i in f:
            data.append(i)
        return data


def calculate_statistics(line):
    value = []
    value.extend(line)
    l = len(value)                      # количество значений
    mean = statistics.mean(value)       # среднее значение
    mode = statistics.mode(value)       # мода
    median = statistics.median(value)   # медиана
    return l, mean, mode, median


if len (sys.argv) < 3:
    print('Ошибка: недостаточное количество аргументов. Завершение программы.')
    exit()

con_file = sys.argv[1] # чтение файла для обработки
con_time = sys.argv[2] # чтение интервала разбиения

data = read_data_from_file(con_file)
segment = split_data.split_data(data, con_time)
for line in segment:
    l, mean, mode, median = calculate_statistics(line)
    print(  ' количество значений = ', l, ';',
            ' среднее значение = ', mean, ';',
            ' мода = ', mode, ';' ,
            ' медиана = ', median, ';',
            sep = '')
