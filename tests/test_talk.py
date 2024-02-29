import pytest
from my_little_package import talk


def test_talk(capsys):
    talk.greeting("Adam")
    captured = capsys.readouterr()
    assert captured.out == "Hello Adam!\n"


# expected to fail
@pytest.mark.xfail()
def test_talk_bad():
    talk.greeting(1)
