import pytest
from my_little_package import talk


def test_talk():
    talk.greeting("Adam")


# expected to fail
@pytest.mark.xfail()
def test_talk_bad():
    talk.greeting(1)
