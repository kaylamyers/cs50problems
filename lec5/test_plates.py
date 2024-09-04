from plates import is_valid

def test_twoletstart():
    assert is_valid("CS50") == True
    assert is_valid("50") == False

def test_max6min2():
    assert is_valid("AA") == True
    assert is_valid("AABBCC") == True
    assert is_valid("AABBCCD") == False
    assert is_valid("A") == False

def test_middlenum():
    assert is_valid("AAA222") == True
    assert is_valid("CS50P") == False

def test_zerofirst():
    assert is_valid("AA20") == True
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("AA.B") == False
    assert is_valid("!?B2") == False
    assert is_valid("AA B !") == False


