# Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
from typing import Dict
from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index: Dict[int, int] = {}
        for index, num in enumerate(nums):
            goal = target - num
            if goal in num_to_index:
                return [num_to_index[goal], index]
            num_to_index[num] = index

        return [0, 0]


@pytest.mark.parametrize(
    ("nums", "target", "expected"), [([2, 7, 11, 15], 9, [0, 1])],
)
def test_two_sum(nums: List[int], target: int, expected: List[int]) -> None:
    assert Solution().twoSum(nums, target) == expected
