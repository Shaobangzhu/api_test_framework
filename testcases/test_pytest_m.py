import pytest


class TestPytest:
    # 1. run pytest -s testcases/test_pytest_m.py
    # 2. run pytest -s testcases/test_pytest_m.py::TestPytest::test_extron
    # 3. run pytest -s -m extron
    # 4. run pytest -s -k pytest
    @pytest.mark.google
    def test_google(self):
        print("google", "https://www.google.com/")

    @pytest.mark.extron
    def test_extron(self):
        print("extron", "https://www.extron.com/")