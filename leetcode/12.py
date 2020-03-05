# 12. Integer to Roman
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
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.


def int_to_roman(num: int) -> str:
    ONES_MAP = {
        0: "",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
    }

    TENS_MAP = {
        0: "",
        1: "X",
        2: "XX",
        3: "XXX",
        4: "XL",
        5: "L",
        6: "LX",
        7: "LXX",
        8: "LXXX",
        9: "XC",
    }

    HUNDREDS_MAP = {
        0: "",
        1: "C",
        2: "CC",
        3: "CCC",
        4: "CD",
        5: "D",
        6: "DC",
        7: "DCC",
        8: "DCCC",
        9: "CM",
    }

    THOUSANDS_MAP = {
        0: "",
        1: "M",
        2: "MM",
        3: "MMM",
    }

    ones = num % 10
    tens = (num // 10) % 10
    hundreds = (num // 100) % 10
    thousands = (num // 1000) % 10

    return (
        THOUSANDS_MAP[thousands]
        + HUNDREDS_MAP[hundreds]
        + TENS_MAP[tens]
        + ONES_MAP[ones]
    )


class Solution:
    def intToRoman(self, num: int) -> str:
        return int_to_roman(num)


try:
    import pytest

    @pytest.mark.parametrize(
        ("num", "expected"),
        [(1, "I"), (3, "III"), (4, "IV"), (9, "IX"), (58, "LVIII"), (1994, "MCMXCIV"),],
    )
    def test_int_to_roman(num: int, expected: str) -> None:
        assert int_to_roman(num) == expected


except ModuleNotFoundError:
    pass
