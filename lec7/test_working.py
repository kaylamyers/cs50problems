from working import convert
import pytest

def test_correct():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'
    assert convert('10:30 PM to 8 AM') == '22:30 to 08:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'
    assert convert('12 PM to 12 AM') == '12:00 to 00:00'
    assert convert('11:59 PM to 12:01 AM') == '23:59 to 00:01'


def test_sixty():
    with pytest.raises(ValueError):
        assert convert('9:60 AM to 5:60 PM')

def test_dash():
    with pytest.raises(ValueError):
        assert convert('9 AM - 5 PM')

def test_seventeen():
    with pytest.raises(ValueError):
        assert convert('09:00 AM - 17:00 PM')