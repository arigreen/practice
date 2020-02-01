# 6. ZigZag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
import itertools
from typing import Generator
from typing import Iterator

import pytest


def convert(s: str, num_rows: int) -> str:
    def gen_row(row: int) -> Generator[str, None, None]:
        index = row
        downward = True
        while index < len(s):
            yield s[index]
            if row == 0 or row == num_rows - 1:
                index += 2 * (num_rows - 1)
            else:
                if downward:
                    index += 2 * (num_rows - 1 - row)
                else:
                    index += 2 * (row)
                downward = not downward

    def gen_all() -> Iterator[str]:
        return itertools.chain(*[gen_row(row) for row in range(num_rows)])

    return "".join(char for char in gen_all())


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return convert(s, numRows)


@pytest.mark.parametrize(
    ("input_s", "num_rows", "expected"),
    [
        ("", 0, ""),
        ("", 1, ""),
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ],
)
def test_convert(input_s: str, num_rows: int, expected: str) -> None:
    assert convert(input_s, num_rows) == expected
