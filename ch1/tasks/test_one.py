import random

import pytest


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.custom
def test_custom():
    lst = [i for i in range(10)]
    random_number = random.randint(0, 9)
    assert random_number in lst
