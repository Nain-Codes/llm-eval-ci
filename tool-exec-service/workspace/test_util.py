from util import safe_add

def test_safe_add():
    assert safe_add(2, 3) == 5
    assert safe_add(-1, 1) == 0
