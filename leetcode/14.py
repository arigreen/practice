# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List


def longest_common_prefix_simple(strs: List[str]) -> str:
    # 32 ms, faster than 66.67%
    # For increasing values of i, starting at i=0, compare the ith character of
    # each string, until we find a non-match.
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    length = 0
    while True:
        if len(strs[0]) <= length:
            break
        if not all(
            [len(s) > length and strs[0][length] == s[length] for s in strs[1:]]
        ):
            break
        length += 1

    return strs[0][:length]


def longest_common_prefix_sorted(strs: List[str]) -> str:
    # Sort the strings, then compare characters in the first string to
    # characters in the last string until we find a non-match
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    sorted_strs = sorted(strs)
    first, last = sorted_strs[0], sorted_strs[-1]
    max_length = min(len(first), len(last))
    length = 0
    for i in range(max_length):
        if first[length] != last[length]:
            break
        length += 1
    return sorted_strs[0][:length]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return longest_common_prefix_simple(strs)


try:
    import pytest

    @pytest.mark.parametrize(
        ("strs", "expected"),
        [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], ""),],
    )
    def test_longest_common_prefix(strs: List[str], expected: str) -> None:
        assert longest_common_prefix_simple(strs) == expected
        assert longest_common_prefix_sorted(strs) == expected


except ModuleNotFoundError:
    pass
