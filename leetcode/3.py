# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
from typing import Set

import pytest


def length_of_longest_substring_brute_force(s: str) -> int:
    if not s:
        return 0

    def length_starting_at_position(pos: int) -> int:
        result = 0
        seen: Set[str] = set()
        for index in range(pos, len(s)):
            if s[index] in seen:
                break
            seen.add(s[index])
            result += 1
        return result

    return max(length_starting_at_position(pos) for pos in range(len(s)))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return length_of_longest_substring_brute_force(s)


@pytest.mark.parametrize(
    ("s", "expected"), [("", 0), ("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]
)
def test_length_of_longest_substring(s: str, expected: int) -> None:
    assert length_of_longest_substring_brute_force(s) == expected
