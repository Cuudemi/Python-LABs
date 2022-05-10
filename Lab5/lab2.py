import csv
import statistics
import sys
import split_data
import os
from os import path


def read_data_from_file(file) -> list:
    """ Данная функция читает файл csv с пропуском первой строки и возвращает массив строк """
    if (os.access(file, os.F_OK) == False):
        raise FileNotFoundError("данного файла не существует. Завершение программы")
        # print ("Ошибка: данного файла не существует")
        # return -1

    if (os.access(file, os.R_OK)):
        full_name = path.basename(file)
        name = path.splitext(full_name)[1]
        if (name == '.csv'):
            data = []
            with open(file, 'r') as file:
                next(file)
                f = csv.reader(file, dialect="excel")
                for i in f:
                    data.append(i)
                return data
        else:
            raise TypeError("неверный формат файла. Завершение программы")
            #print ("Ошибка: неверный формат файла:", name, "вместо .csv. Завершение программы.")
            #return -3
    else:
        raise TypeError("нет прав чтения. Завершение программы")
        #print ("Ошибка: файл не имеет прав на чтение. Завершение программы.")
        #return -2


def calculate_statistics(line):
    value = []
    value.extend(line)
    l = len(value)                      # количество значений
    mean = statistics.mean(value)       # среднее значение
    mode = statistics.mode(value)       # мода
    median = statistics.median(value)   # медиана
    return l, mean, mode, median




if __name__== '__main__':
    if len (sys.argv) < 3:
        print('Ошибка: недостаточное количество аргументов. Завершение программы.')
        exit(1)

    con_file = sys.argv[1]
    con_time = sys.argv[2]

    data = read_data_from_file(con_file)
    #if len(str(data)) == 2:
        #exit(1)

    segment = split_data.split_data(data, con_time)
    print(len(segment))
    #if len(str(segment)) == 2:
        #exit(1)

    for line in segment:
        l, mean, mode, median = calculate_statistics(line)
        print(  ' Количество значений = ', l, ';',
                    ' среднее значение = ', mean, ';',
                    ' мода = ', mode, ';' ,
                    ' медиана = ', median, ';',
                    sep = '')
