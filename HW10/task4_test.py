# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures("test_time_start_to_end")
class TestFindTime:

    def test_first(self):
        assert True

    def test_second(self):
        assert True

    def test_third(self, test_time_continue):
        assert True

