# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# Note:
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
from typing import Dict
from typing import Tuple

import pytest

CacheKey = Tuple[str, str]


def is_match(s: str, p: str, cache: Dict[CacheKey, bool]) -> bool:
    # 36 ms, faster than 93.28%
    if (s, p) in cache:
        return cache[(s, p)]

    first_char_match = bool(len(s) and len(p) and p[0] in [".", s[0]])

    if len(p) == 0:
        result = len(s) == 0
    elif not p[0].isalpha() and p[0] != ".":
        raise Exception("Invalid pattern")

    elif len(p) == 1:
        result = len(s) == 1 and first_char_match

    # 3 cases depending on if second char is a-z, '.', or '*'
    elif p[1] != "*":
        result = first_char_match and is_match(s[1:], p[1:], cache)
    elif is_match(s, p[2:], cache):
        result = True
    # 2. Use 1+ copies of p[0]. This can only be done if s[0] == p[0]
    else:
        result = first_char_match and is_match(s[1:], p, cache)

    cache[(s, p)] = result
    return result


def is_match_dp(s: str, p: str) -> bool:
    # 32 ms, faster than 97.78%

    cache: Dict[Tuple[int, int], bool] = {}

    def solve_dp(s_index: int, p_index: int) -> bool:
        """
        Return True if s[s_index:] matches p[p_index:]
        """
        if (s_index, p_index) in cache:
            return cache[(s_index, p_index)]

        s_substr_len = len(s) - s_index
        p_substr_len = len(p) - p_index

        # Indicates if the first character of the string matches the first
        # character of the pattern
        first_char_match = (
            s_substr_len and p_substr_len and p[p_index] in [".", s[s_index]]
        )

        if p_substr_len == 0:
            result = s_substr_len == 0
        elif p_substr_len == 1:
            result = bool(s_substr_len == 1 and first_char_match)
        elif p[p_index + 1] != "*":
            result = bool(first_char_match and solve_dp(s_index + 1, p_index + 1))
        else:
            # There is a '*' in the second position, so a match can occur if we
            # consume the first character or if we don't consume the first
            # character
            result = solve_dp(s_index, p_index + 2) or bool(
                first_char_match and solve_dp(s_index + 1, p_index)
            )

        cache[(s_index, p_index)] = result
        return result

    return solve_dp(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return is_match_dp(s, p)


@pytest.mark.parametrize(
    ("s", "p", "expected"),
    [
        ("", "", True),
        ("a", "", False),
        ("", "a", False),
        ("b", "a*b", True),
        ("ab", "a*b", True),
        ("aab", "a*b", True),
        ("aa", "a", False),
        ("aa", "a*", True),
        ("aa", ".a", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
    ],
)
def test_is_match(s: str, p: str, expected: bool) -> None:
    assert is_match(s, p, {}) == expected
    assert is_match_dp(s, p) == expected
