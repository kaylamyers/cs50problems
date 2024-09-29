from um import count

def test_zero():
    assert count("hello") == 0
    assert count("album") == 0
    assert count("ummmmm") == 0

def test_one():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um, thanks for the album") == 1
    assert count("UM, HELLO?!") == 1

def test_twoPlus():
    assert count("um, thanks, um") == 2
    assert count("...um!  um...") == 2

