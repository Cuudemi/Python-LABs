import csv
import statistics
import sys
import split_data
import os
from os import path

# !!!!
# помнится, Петрина придиралась к единицам измерения
# времени и поэтому тебе пришлось преобразовывать время
# в минуты. сдавая лабу у своего преподавателя, я всё это
# подтерла, так что тебе нужно снова преобразовать время
# (делением на 60?). возможно, оно осталось в коде 
# второй лабораторной. но тогда нужно, возможно, поправить
# последние три тестика. если будут вопросы -- то пиши


# raise вызывает конкретную ошибку, которую мы ему
# напишем, когда что-то пойдет не так. советую намеренно
# запустить программму с неверными аргументами и посмотреть,
# как оно работает. плюс этого raise в том, что файлик
# лабораторной может работать обособленно от файлика с
# тестированием, ловя и сообщая о ошибках самостоятельно.
# выглядит здорово

def read_data_from_file(file) -> list:
    """ Данная функция читает файл csv с пропуском первой строки и возвращает массив строк """
    if (os.access(file, os.F_OK) == False):
        raise FileNotFoundError("данного файла не существует. Завершение программы")

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
    else:
        raise TypeError("нет прав чтения. Завершение программы")


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

    segment = split_data.split_data(data, con_time)
    print(len(segment))

    for line in segment:
        l, mean, mode, median = calculate_statistics(line)
        print(  ' Количество значений = ', l, ';',
                    ' среднее значение = ', mean, ';',
                    ' мода = ', mode, ';' ,
                    ' медиана = ', median, ';',
                    sep = '')
