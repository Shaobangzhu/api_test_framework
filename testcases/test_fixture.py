import pytest


class TestPytest:
    @pytest.fixture(scope="function")
    def front(self):
        # return "https://"
        yield "https://"
        print("测试结束")

    @pytest.mark.google
    def test_google(self, front):
        print("google", f"{front}www.google.com/")

    @pytest.mark.extron
    def test_extron(self, front):
        print("extron", f"{front}www.extron.com/")