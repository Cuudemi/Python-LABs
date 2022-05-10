from token import TYPE_IGNORE
import split_data
from lab2 import read_data_from_file
from split_data import *
from lab2 import *
import pytest


def test_no_file():
    """ Тест на отсутствие файла """
    with pytest.raises(FileNotFoundError):
        read_data_from_file("non-existent_file.csv")


def test_no_roots():
    """ Тест на то, имеет ли файл права на чтение """
    with pytest.raises(TypeError):
        read_data_from_file("no_r.csv")


def test_csv_format():
    """ Тест на требуемый формат файла (csv) """
    with pytest.raises(TypeError):
        read_data_from_file("3.jpg")


def test_column():
    """ Тест на правильное количество колонок (две) """
    with pytest.raises(IndexError):
        split_data.split_data("1_columnn.csv", 3)


def test_data():
    """ Тест на верный тип данных """
    with pytest.raises(ValueError):
        split_data.split_data("data.csv", 3)


def test_integrals():
    """ Тест на верные по времени интегралы """
    data = read_data_from_file("check.csv")
    segment = split_data.split_data(data, 5)
    for line in segment:
        if ((line[len(line)-1]) - line[0] <= 5):
            assert True


def test_num_of_integrals():
    """ Тест на правильное количество интегралов """
    data = read_data_from_file("check.csv")
    segment = split_data.split_data(data, 8)
    assert len(segment) == 6


def test_statistics():
    """ Тест на правильный подсчёт статистики """
    data = read_data_from_file("check.csv")
    segment = split_data.split_data(data, 60)
    for line in segment:
        l, mean, mode, median = calculate_statistics(line)
        assert l == 50
        assert mean == 25.5
        assert mode == 50
        assert median == 25.5
