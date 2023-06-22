# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('args, result', [pytest.param([25, 5], 5, marks=pytest.mark.smoke), ([56, 2, 4], 7),
                                          pytest.param([0, 20], 0, marks=pytest.mark.skip(reason='wait to task №123')),
                                          ([73.5, 2.5], 29.4), ([-44.4, 2], -22.2)])


def test_int(args, result):
    assert all_division(*args) == result
