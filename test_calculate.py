import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2,3,5),
    (3,7,10),
    (-2,5,3)
])

@pytest.mark.parametrize("c,d,expected", [
    (4,1,3),
    (1,9,-8),
    (5,6,-1)
])

def test_add(a,b,expected):
    from calculate import add 
    result = add(a,b)
    assert result == pytest.approx(expected)

def test_subtract(c,d,expected):
    from calculate import subtract
    result = subtract(c,d)
    assert result == expected