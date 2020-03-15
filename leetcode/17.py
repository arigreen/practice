# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
from typing import List

MAPPING = {
    0: "",
    1: "",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}


def recursive_combinations(prefix: str, digits: List[int]) -> List[str]:
    results: List[str] = []
    if not digits:
        return [prefix]
    first_letters = list(MAPPING[digits[0]])
    for first_letter in first_letters:
        results = results + recursive_combinations(prefix + first_letter, digits[1:])
    return results


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits_list = [int(digit) for digit in digits]
        return recursive_combinations("", digits_list)


try:
    import pytest

    @pytest.mark.parametrize(
        ("digits", "expected"),
        [("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])],
    )
    def test_letter_combinations(digits: str, expected: List[str]) -> None:
        assert sorted(Solution().letterCombinations(digits)) == sorted(expected)


except ModuleNotFoundError:
    pass
