from seasons import minutes
import pytest

def test_correct():
    assert minutes('2023-10-17') == 'Five hundred twenty-seven thousand forty minutes'
    assert minutes('2022-10-17') == 'One million, fifty-two thousand, six hundred forty minutes'


def test_sixty():
    with pytest.raises(SystemExit):
        assert minutes('September 28, 2024')

