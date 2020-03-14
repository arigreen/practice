# 15. 3Sum
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.
from collections import Counter
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    results: List[List[int]] = []

    c = Counter(nums)
    for first_num in c.keys():
        third_to_second = {}
        for second_num in c.keys():
            if second_num < first_num or second_num == first_num and c[second_num] < 2:
                continue
            target = 0 - first_num - second_num
            if target < second_num:
                continue
            third_to_second[target] = second_num
        for third_num, second_num in third_to_second.items():
            if third_num in c:
                if (
                    third_num == second_num
                    and third_num == first_num
                    and c[third_num] < 3
                ):
                    continue
                if third_num == second_num and c[third_num] < 2:
                    continue
                results.append(sorted([first_num, second_num, third_num]))

    print(results)
    return results


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return three_sum(nums)


try:
    import pytest

    @pytest.mark.parametrize(
        ("nums", "expected"),
        [
            ([-1, 0, 1, 2, -1, 4], [[-1, -1, 2], [-1, 0, 1]]),
            ([-1, 1, 2, -1, 4], [[-1, -1, 2]]),
            ([-1, -1, 2], [[-1, -1, 2]]),
            ([], []),
            ([0, 0, 0], [[0, 0, 0]]),
        ],
    )
    def test_three_sum(nums: List[int], expected: List[List[int]]) -> None:
        assert three_sum(nums) == expected


except ModuleNotFoundError:
    pass
