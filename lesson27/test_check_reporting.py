import pytest


def test_check_sum():
    assert 2 + 2 == 4

def test_check_multiply():
    assert 2 * 2 == 4

@pytest.mark.skip
def test_to_skip():
    pass