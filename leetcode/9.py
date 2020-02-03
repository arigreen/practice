# 9. Palindrome Number
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
import pytest


def reverse(x: int) -> int:
    result = 0
    while x:
        last_digit = x % 10
        x = x // 10
        result = result * 10 + last_digit
    return result


def is_palindrome(x: int) -> bool:
    return x >= 0 and x == reverse(x)


class Solution:
    def isPalindrome(self, x: int) -> int:
        return is_palindrome(x)


@pytest.mark.parametrize(
    ("x", "expected"),
    [(-1, False), (-121, False), (121, True), (123, False), (0, True), (10, False),],
)
def test_is_palindrome(x: int, expected: bool) -> None:
    assert is_palindrome(x) == expected
