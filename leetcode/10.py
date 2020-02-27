# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# Note:
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
import pytest


def is_match(s: str, p: str) -> bool:
    if len(p) == 0:
        return len(s) == 0
    if not p[0].isalpha() and p[0] != ".":
        raise Exception("Invalid pattern")

    if len(p) == 1:
        return len(s) == 1 and p in [".", s]

    # 3 cases depending on if second char is a-z, '.', or '*'
    if p[1] != "*":
        return len(s) > 0 and (s[0] == p[0] or p[0] == ".") and is_match(s[1:], p[1:])

    else:
        # 2 cases:
        # 1. Use 0 copies of p[0]
        if is_match(s, p[2:]):
            return True

        # 2. Use 1+ copies of p[0]. This can only be done if s[0] == p[0]
        if len(s) > 0 and (p[0] == s[0] or p[0] == ".") and is_match(s[1:], p):
            return True

        return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return is_match(s, p)


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
    assert is_match(s, p) == expected
