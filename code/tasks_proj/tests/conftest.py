import pytest
import tasks
from tasks import Task


@pytest.fixture()
def tasks_db(tmpdir):
    """Подключение к БД перед тестами, отключение после."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # здесь происходит тестирование

    # Teardown : stop db
    tasks.stop_tasks_db()
