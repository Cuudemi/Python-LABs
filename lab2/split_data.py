def split_data(data, time):
    """ Данная функция разбивает полученные данные data на отрезки с интервалом времени time """
    i = 0
    interval = int(time)
    segment = [[]]
    time = interval
    for line in data:
        time_data = float(line[0])
        value_data = int(line[1])
        if (time_data) // 60 <= time:
            segment[i].append(value_data)
        else:
            if len(segment[i]) != 0:
                i += 1
                segment.append([])
            segment[i].append(value_data)
            time = (time_data) // 60 + interval

    return segment