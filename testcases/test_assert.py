import pytest
from pytest_assume.plugin import assume

class TestAssert:
    def test_assert(self):
        pytest.assume(1 + 1 == 3)
        assert 1 + 1 == 2
        with assume: assert 3 < 2
        with assume: assert "william" in "william API autotest"
        print("over")