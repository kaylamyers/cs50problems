from twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("TwiTtER") == "TwTtR"

def test_space():
    assert shorten("What's your Twitter") == "Wht's yr Twttr"

def test_num():
    assert shorten("CS.50") == "CS.50"