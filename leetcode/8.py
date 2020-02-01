# 8. String to Integer (atoi)
"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the
first non-whitespace character is found.

Then, starting from this character, takes an optional initial plus or minus sign
followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace
characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−2^31,  2^31 − 1].
If the numerical value is out of the range of representable values, INT_MAX
(2^31 − 1) or INT_MIN (−2^31) is returned.
"""
import pytest

INT_MAX = (2 << 30) - 1
INT_MIN = -2 << 30

ORD_0 = ord("0")


def atoi(s: str) -> int:
    s = s.lstrip(" ")
    if not s:
        return 0

    result = 0
    sign = 1

    if s[0] == "+":
        s = s[1:]
    elif s[0] == "-":
        s = s[1:]
        sign = -1

    for c in s:
        if not c.isdigit():
            break
        result = result * 10 + (ord(c) - ORD_0)
        # Check for overflow
        if result * sign <= INT_MIN:
            return INT_MIN
        if result * sign >= INT_MAX:
            return INT_MAX

    return result * sign


class Solution:
    def myAtoi(self, str: str) -> int:
        return atoi(str)


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("123", 123),
        ("-123", -123),
        ("120", 120),
        ("+1", 1),
        (" 43", 43),
        ("43 with words", 43),
        ("2147483647", 2147483647),
        ("2147483648", 2147483647),
        ("-2147483647", -2147483647),
        ("-2147483648", -2147483648),
        ("-2147483649", -2147483648),
    ],
)
def test_atoi(s: str, expected: int) -> None:
    assert atoi(s) == expected
