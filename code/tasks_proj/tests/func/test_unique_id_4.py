import pytest

import tasks


@pytest.mark.xfail(tasks.__version__ < '0.2.0',
                   reason='not supported until version 0.2.0')
def test_unique_id_1():
    """Вызов unique_id() дважды должен возвращать разные номера."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Продемонстрирация xfail."""
    uid = tasks.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Продемонстрирация xpass."""
    uid = tasks.unique_id()
    assert uid != 'a duck'
