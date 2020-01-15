# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
from typing import Set

import pytest


def length_of_longest_substring_brute_force(s: str) -> int:
    # 432 ms on LeetCode
    if not s:
        return 0

    def length_starting_at_position(pos: int) -> int:
        result = 0
        seen: Set[str] = set()
        for c in s[pos:]:
            if c in seen:
                break
            seen.add(c)
            result += 1
        return result

    return max(length_starting_at_position(pos) for pos in range(len(s)))


def length_of_longest_substring_onepass(s: str) -> int:
    # 52 ms on LeetCode
    max_length = 0
    current_substring = ""
    for c in s:
        pos = current_substring.find(c)
        if pos >= 0:
            max_length = max(max_length, len(current_substring))
            current_substring = current_substring[pos + 1 :]

        current_substring += c

    max_length = max(max_length, len(current_substring))

    return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return length_of_longest_substring_onepass(s)


@pytest.mark.parametrize(
    ("s", "expected"),
    [("", 0), ("aab", 2), ("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)],
)
def test_length_of_longest_substring(s: str, expected: int) -> None:
    assert length_of_longest_substring_brute_force(s) == expected
    assert length_of_longest_substring_onepass(s) == expected
