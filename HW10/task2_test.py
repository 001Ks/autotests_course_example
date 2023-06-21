# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_int():
    assert all_division(25, 5) == 5


@pytest.mark.smoke
def test_float():
    assert all_division(73.5, 2.5) == 29.4


def test_int_lower_zero():
    assert all_division(-44.4, 2) == -22.2


def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(2, 0)


def test_more_two_int():
    assert all_division(56, 2, 4) == 7

