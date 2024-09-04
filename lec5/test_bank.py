from bank import value

def test_hello():
    assert value("Hello") == 0

def test_hey():
    assert value("hey") == 20

def test_yo():
    assert value("yo") == 100