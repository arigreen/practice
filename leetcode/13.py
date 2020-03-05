# 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II.
# The number twenty seven is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII.
# Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


def roman_to_int(roman: str) -> int:
    prev = None
    result = 0
    for char in roman:
        if char == "I":
            result += 1
        elif char == "V":
            result += 5
        elif char == "X":
            result += 10
        elif char == "L":
            result += 50
        elif char == "C":
            result += 100
        elif char == "D":
            result += 500
        elif char == "M":
            result += 1000

        if char in ["V", "X"] and prev == "I":
            result -= 2 * 1
        elif char in ["L", "C"] and prev == "X":
            result -= 2 * 10
        elif char in ["D", "M"] and prev == "C":
            result -= 2 * 100

        prev = char

    return result


class Solution:
    def romanToInt(self, roman: str) -> int:
        return roman_to_int(roman)


try:
    import pytest

    @pytest.mark.parametrize(
        ("roman", "expected"),
        [("I", 1), ("III", 3), ("IV", 4), ("IX", 9), ("LVIII", 58), ("MCMXCIV", 1994),],
    )
    def test_roman_to_int(roman: str, expected: int) -> None:
        assert roman_to_int(roman) == expected


except ModuleNotFoundError:
    pass
