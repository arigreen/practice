# 16. 3Sum Closest
# Given an array nums of n integers and an integer target, find three integers in nums such that the sum
# is closest to target. Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            raise Exception("Not enough integers")
        nums = sorted(nums)

        closest_sum = nums[0] + nums[1] + nums[2]

        for first_index, first_num in enumerate(nums):
            left_index = first_index + 1
            right_index = len(nums) - 1

            while left_index < right_index:
                left_num = nums[left_index]
                right_num = nums[right_index]
                sum = first_num + left_num + right_num
                if abs(target - sum) < abs(target - closest_sum):
                    closest_sum = sum
                if sum < target:
                    # to get closer we must increase left
                    left_index += 1
                elif sum > target:
                    right_index -= 1
                else:
                    # We found an exact match
                    return sum

        return closest_sum


try:
    import pytest

    @pytest.mark.parametrize(
        ("nums", "target", "expected"), [([-1, 2, 1, -4], 1, 2),],
    )
    def test_three_sum_closest(nums: List[int], target: int, expected: int) -> None:
        assert Solution().threeSumClosest(nums, target) == expected


except ModuleNotFoundError:
    pass
