import math
import pytest
from mini_calc import add, sub, mean, is_prime


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-5, 5, 0),
    (2.5, 0.5, 3.0),
    (5.5, 0.5, 6.0),
])
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a,b,expected", [
    (3, 2, 1),
    (2, 3, -1),
    (-1, -1, 0),
])
def test_sub(a, b, expected):
    assert sub(a, b) == pytest.approx(expected)


def test_mean_basic():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_raises_on_empty():
    with pytest.raises(ValueError):
        mean([])


@pytest.mark.parametrize("n,expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (19, True),
    (20, False),
    (97, True),
])
def test_is_prime(n, expected):
    assert is_prime(n) is expected
