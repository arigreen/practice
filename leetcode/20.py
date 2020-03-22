# 20. Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
from utils import timing


class Solution:
    def isValid(self, s: str) -> bool:
        CLOSE_TO_OPEN = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for c in s:
            if c in CLOSE_TO_OPEN.values():
                stack.append(c)
            elif c in CLOSE_TO_OPEN.keys():
                if not stack or stack.pop() != CLOSE_TO_OPEN[c]:
                    return False
            else:
                raise Exception("Invalid input")

        # After exhausting the input, return True only if the stack is empty
        return not bool(stack)


try:
    import pytest

    @pytest.mark.parametrize(
        ("s", "expected"),
        [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("([)]", False),
            ("{[]}", True),
        ],
    )
    def testIsValid(s: str, expected: bool) -> None:
        with timing(f"test"):
            assert Solution().isValid(s) == expected


except ModuleNotFoundError:
    pass
