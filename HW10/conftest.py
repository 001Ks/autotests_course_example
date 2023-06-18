import pytest
import time

@pytest.fixture
def test_time_start_to_end():
    time_start = time
    yield
    time_finish = time
    assert f'Время начала {time_start}, Время конца {time_finish}'

@pytest.fixture
def test_time_continue():
    time_start = time
    yield
    time_finish = time
    assert f'Выполнилось за {time_finish}-{time_start} '

