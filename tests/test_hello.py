from pytest import fixture


@fixture
def message():
    return "Hello World"


def test(message):
    assert message == "Hello World"
