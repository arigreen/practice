# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of
# well-formed parentheses.
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
from typing import List

from utils import timing


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Recursive backtracking search.
        Generate the string from left to right by considering all prefixes that are valid.
        A prefix is valid if it contains n or fewer left parens and there are no positions
        within the string where the number of right parens exceeds the number of left parens.
        """
        results = []

        def genHelper(prefix: str, num_left: int, num_right: int) -> None:
            if num_left < n:
                genHelper(prefix + "(", num_left + 1, num_right)
            if num_right < num_left:
                genHelper(prefix + ")", num_left, num_right + 1)
            if num_left == n and num_right == n:
                results.append(prefix)

        genHelper("", 0, 0)
        return results


try:
    import pytest

    @pytest.mark.parametrize(
        ("n", "expected"),
        [
            (0, [""]),
            (1, ["()"]),
            (2, ["(())", "()()"]),
            (3, ["((()))", "()(())", "()()()", "(()())", "(())()"]),
        ],
    )
    def testGenerateParenthesis(n: int, expected: List[str]) -> None:
        with timing(f"recursive"):
            result = Solution().generateParenthesis(n)
        assert len(result) == len(expected)
        assert set(result) == set(expected)


except ModuleNotFoundError:
    pass
