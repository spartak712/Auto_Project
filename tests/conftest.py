import pytest

from base.base import Base

"""Фикстура - выполняется при каждом тесте"""
@pytest.fixture
def setup():
    print("\nTest started")
    base = Base
    base.browser.get(base.base_url)
    base.browser.maximize_window()
    print("Opened web-site")
    base.get_current_url(base)
    yield
    print("Test finished")