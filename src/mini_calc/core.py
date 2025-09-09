from typing import Iterable


def add(a: float, b: float) -> float:
    """Zwraca sumę a + b."""
    return a + b


def sub(a: float, b: float) -> float:
    """Zwraca różnicę a - b."""
    return a - b


def mean(numbers: Iterable[float]) -> float:
    """Zwraca średnią arytmetyczną z iterowalnej kolekcji liczb.

    Raises
    ------
    ValueError
        Jeśli kolekcja jest pusta.
    """
    nums = list(numbers)
    if not nums:
        raise ValueError("Cannot compute mean of empty sequence")
    return sum(nums) / len(nums)


def is_prime(n: int) -> bool:
    """Zwraca True jeśli n jest liczbą pierwszą, w przeciwnym razie False."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    step = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += step
        step = 6 - step
    return True
