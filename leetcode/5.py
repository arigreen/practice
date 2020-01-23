# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
from typing import List

import pytest


def longest_palindrome_from_middle(s: str) -> str:
    # 1664 ms, faster than 47.77% of Python3 online submissions
    """
    For each index, compute:
        longest palindrome of odd length centered at that index, e.g. abCba
        longest palindrome of even length centered at that index, e.g. abCcba
    """
    longest = ""
    for index, c in enumerate(s):
        # odd length palindromes
        num_side = 0
        while True:
            if index - num_side - 1 < 0 or index + num_side + 1 >= len(s):
                break
            if s[index - num_side - 1] != s[index + num_side + 1]:
                break
            num_side += 1
        if num_side * 2 + 1 > len(longest):
            longest = s[index - num_side : index + num_side + 1]

        # even length palindrome, where c is the first of the 2 middle chars
        if index + 1 < len(s) and c == s[index + 1]:
            num_side = 0
            while True:
                if index - num_side - 1 < 0 or index + 2 + num_side >= len(s):
                    break
                if s[index - num_side - 1] != s[index + 2 + num_side]:
                    break
                num_side += 1
            if (num_side + 1) * 2 > len(longest):
                longest = s[index - num_side : index + num_side + 2]

    return longest


def longest_palindrome_dp(s: str) -> str:
    # 5088 ms, faster than 19.85% of Python3 online submissions
    size = len(s)
    if size <= 1:
        return s

    is_palindrome_array = [x[:] for x in [[False] * size] * size]
    longest = s[0]
    for length in range(1, size + 1):
        for start in range(size):
            i = start
            j = start + length - 1
            if j >= size:
                break

            if s[i] == s[j] and (i + 1 >= j or is_palindrome_array[i + 1][j - 1]):
                is_palindrome_array[i][j] = True
                if length > len(longest):
                    longest = s[i : j + 1]
    return longest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return longest_palindrome_from_middle(s)


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("", [""]),
        ("a", ["a"]),
        ("aa", ["aa"]),
        ("ab", ["a", "b"]),
        ("aaa", ["aaa"]),
        ("aab", ["aa"]),
        ("aba", ["aba"]),
        ("bba", ["bb"]),
        ("abc", ["a", "b", "c"]),
        ("aaaa", ["aaaa"]),
        ("abba", ["abba"]),
        ("abcdeedcba", ["abcdeedcba"]),
        ("babad", ["bab", "aba"]),
        ("anana", ["anana"]),
        ("ananan", ["anana", "nanan"]),
        ("aabaaa", ["aabaa"]),
        ("ananana", ["ananana"]),
    ],
)
def test_longest_palindrome(s: str, expected: List[str]) -> None:
    assert longest_palindrome_from_middle(s) in expected
    assert longest_palindrome_dp(s) in expected
