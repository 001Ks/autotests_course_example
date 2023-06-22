import pytest
import time


@pytest.fixture
def test_time_start_to_end():
    time_start = time.time()
    yield
    time_finish = time.time()
    print(f'Время начала {time.ctime(time_start)}, Время конца {time.ctime(time_finish)}')

@pytest.fixture
def test_time_continue():
    time_start = time.time()
    yield
    time_finish = time.time()
    print(f'Выполнилось за {round((time_finish - time_start) * 1000, 3)} ms')

