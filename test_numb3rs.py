from numb3rs import validate

def test_zeros():
    assert validate("0.0.0.0") == True
    assert validate("00.00.00.00") == True
    assert validate("000.000.000.000") == True

def test_true():
    assert validate("255.255.255.255") == True
    assert validate("255.255.255.0") == True
    assert validate("127.0.0.1") == True
    assert validate("2.5.60.200") == True

def test_false():
    assert validate("100.1000.100.0") == False
    assert validate("275.3.6.28") == False
    assert validate("25.3.600.28") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("cat.dog.bird.fish") == False
    assert validate("?.!.-.$") == False
    assert validate("1.20.3.40.5.60") == False

