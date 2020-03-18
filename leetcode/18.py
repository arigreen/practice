# 18. 4Sum
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
# such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Note: The solution set must not contain duplicate quadruplets.
# There have been many similar problems: 2-Sum, 3-Sum, and now 4-Sum.
# I will solve the general K-sum solution
from typing import List

from utils import timing


def k_sum(nums: List[int], target: int, k: int) -> List[List[int]]:
    def k_sum_sorted(start_index: int, target: int, k: int) -> List[List[int]]:
        """
        Assumes that nums has been sorted and that k >= 2.
        """
        results: List[List[int]] = []
        if k == 2:
            left = start_index
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    results.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
        else:
            for first_index in range(start_index, len(nums)):
                new_target = target - nums[first_index]
                sub_results = k_sum_sorted(first_index + 1, new_target, k - 1)
                combined_results = [
                    [nums[first_index]] + sub_result for sub_result in sub_results
                ]
                results += combined_results

        return results

    if k <= 0 or k > len(nums):
        results: List[List[int]] = []
    elif k == 1:
        results = [[target]] if target in nums else []
    else:
        nums.sort()
        results = k_sum_sorted(0, target, k)

    # Uniqify results
    return [list(result) for result in {tuple(result) for result in results}]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return k_sum(nums, target, 4)


try:
    import pytest

    @pytest.mark.parametrize(
        ("nums", "target", "k", "expected"),
        [
            ([1, 2, 2, 3], 4, 2, [[1, 3], [2, 2]]),
            (
                [1, 0, -1, 0, -2, 2],
                0,
                4,
                [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]],
            ),
            (
                [
                    -497,
                    -481,
                    -481,
                    -472,
                    -471,
                    -465,
                    -422,
                    -420,
                    -413,
                    -405,
                    -388,
                    -381,
                    -366,
                    -361,
                    -359,
                    -348,
                    -334,
                    -334,
                    -318,
                    -310,
                    -305,
                    -280,
                    -273,
                    -272,
                    -262,
                    -254,
                    -248,
                    -223,
                    -208,
                    -202,
                    -196,
                    -192,
                    -189,
                    -167,
                    -165,
                    -165,
                    -156,
                    -143,
                    -136,
                    -122,
                    -120,
                    -120,
                    -108,
                    -77,
                    -50,
                    -44,
                    -34,
                    -26,
                    -17,
                    -5,
                    13,
                    46,
                    46,
                    53,
                    54,
                    56,
                    66,
                    71,
                    72,
                    75,
                    89,
                    115,
                    130,
                    139,
                    149,
                    151,
                    154,
                    196,
                    209,
                    219,
                    230,
                    240,
                    245,
                    246,
                    253,
                    267,
                    277,
                    289,
                    299,
                    302,
                    303,
                    304,
                    342,
                    349,
                    360,
                    361,
                    361,
                    375,
                    392,
                    400,
                    407,
                    408,
                    408,
                    426,
                    427,
                    429,
                    443,
                    451,
                    481,
                ],
                -5617,
                4,
                [],
            ),
        ],
    )
    def test_k_sum(
        nums: List[int], target: int, k: int, expected: List[List[int]]
    ) -> None:
        with timing(f"nums of size {len(nums)}"):
            assert sorted(k_sum(nums, target, k)) == sorted(expected)


except ModuleNotFoundError:
    pass
