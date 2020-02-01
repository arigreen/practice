# 7. Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.
# Note: Assume we are dealing with an environment which could only store integers within the 32-bit
# signed integer range:
# [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the
# reversed integer overflows.
import pytest


def reverse(num: int) -> int:
    result = 0

    remaining = abs(num)

    while remaining != 0:
        digit = remaining % 10
        result = result * 10 + digit
        remaining //= 10

    if result >= 1 << 31:
        return 0

    if num < 0:
        result *= -1

    return result


class Solution:
    def reverse(self, num: int) -> int:
        return reverse(num)


@pytest.mark.parametrize(
    ("num", "expected"), [(123, 321), (-123, -321), (120, 21), (4294967296, 0),],
)
def test_reverse(num: int, expected: int) -> None:
    assert reverse(num) == expected
