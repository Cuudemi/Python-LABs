def split_data(data, time):
    """ Данная функция разбивает полученные данные data на отрезки с интервалом времени time """
    i = n = 0
    interval = int(time)
    segment = [[]]
    time = interval
    
    for line in data:
        n += 1
        try:
            time_data = float(line[0])
            value_data = int(line[1])
        except ValueError:
            raise ValueError("Ошибка: неверный формат данных, строка №", n, ". Завершение программы.")
        except IndexError:
            raise IndexError("Ошибка: в таблице вместо двух колонок только одна. Завершение программы.")

        if (time_data) <= time:
            segment[i].append(value_data)
        else:
            if len(segment[i]) != 0:
                i += 1
                segment.append([])
            segment[i].append(value_data)
            time = (time_data) + interval

    return segment