class TestAssert:
    def test_assert(self):
        # ==, !, <, >, <=, >=
        assert "william" == "william"
        assert "william-a" != "william-b"
        assert 0 < 1
        assert 2 > 1
        assert 3 <= 7 - 2
        assert 4 >= 1 + 2

        # 包含和不包含
        assert "william" in "william automation"
        assert "william" not in "UI automation"

        # true or false
        assert 1
        assert (9 < 10) is True
        assert not False