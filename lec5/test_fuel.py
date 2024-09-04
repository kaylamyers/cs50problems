from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

def test_divzero():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")
    

