# 4. Median of Two Sorted Arrays
# Given a string, find the length of the longest substring without repeating characters.
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
from typing import List

import pytest


# The key insight is that as long as there are more than 2 elements, for any k
# less than half of the total number of elements, we can remove k elements from
# the left and k elements from the right and the median will not change.


def median(nums: List[int]) -> float:
    """Helper function to return the median of a list."""
    if len(nums) == 0:
        raise Exception("Attempting to take median of empty list")
    middle = len(nums) // 2
    if len(nums) % 2 == 1:
        return nums[middle]
    else:
        return (nums[middle] + nums[middle - 1]) / 2


def median_of_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    # 88 ms, faster than 92.29%
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    if len(nums1) == 0:
        return median(nums2)

    elif len(nums1) == 1:
        num1 = nums1[0]
        if len(nums2) == 1:
            return (num1 + nums2[0]) / 2
        elif len(nums2) == 2:
            if nums2[0] >= num1:
                return nums2[0]
            elif nums2[1] <= num1:
                return nums2[1]
            else:
                return num1
        elif len(nums2) % 2 == 1:
            # len of nums2 is odd
            middle_2_index = len(nums2) // 2
            num2_lower, num2_mid, num2_higher = (
                nums2[middle_2_index - 1],
                nums2[middle_2_index],
                nums2[middle_2_index + 1],
            )
            if num1 <= num2_lower:
                return (num2_lower + num2_mid) / 2
            elif num1 <= num2_higher:
                return (num1 + num2_mid) / 2
            else:
                return (num2_mid + num2_higher) / 2
        else:
            # len of nums2 is even
            #  1    2 4 6 8
            num2_lower = nums2[(len(nums2) // 2) - 1]
            num2_higher = nums2[len(nums2) // 2]
            if num1 <= num2_lower:
                return num2_lower
            elif num1 >= num2_higher:
                return num2_higher
            else:
                return num1
    else:
        # Special case where no elements from nums1 can be removed
        if (
            len(nums1) == 2
            and len(nums2) % 2 == 0
            and nums1[0] >= nums2[(len(nums2) // 2) - 1]
            and nums1[1] <= nums2[len(nums2) // 2]
        ):
            return (nums1[0] + nums1[1]) / 2

        # Special case where no elements from nums2 can be removed
        if len(nums2) == 2 and nums2[0] >= nums1[0] and nums2[1] <= nums1[1]:
            return (nums2[0] + nums2[1]) / 2

        num_to_remove = max(1, len(nums1) // 2 - 1)
        median_1 = median(nums1)
        median_2 = median(nums2)
        if median_1 == median_2:
            return median_1
        elif median_1 < median_2:
            # The median is greater than median_1, so remove elements from the
            # left of nums1 and the right of nums2
            return median_of_two_sorted_arrays(
                nums1[num_to_remove:], nums2[:-num_to_remove],
            )
        else:
            # median_1 > median_2
            # The median is less than median_1, so remove elements from the
            # right of nums1 and the left of nums2
            return median_of_two_sorted_arrays(
                nums1[:-num_to_remove], nums2[num_to_remove:],
            )


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median_of_two_sorted_arrays(nums1, nums2)


@pytest.mark.parametrize(
    ("nums1", "nums2", "expected"),
    [
        ([1], [], 1),
        ([1, 2], [], 1.5),
        ([1, 2, 3], [], 2),
        ([1, 2, 3, 4], [], 2.5),
        ([1], [2, 3, 4], 2.5),
        ([2], [1, 3, 4], 2.5),
        ([1], [2], 1.5),
        ([1, 3], [2], 2),
        ([1, 2], [3], 2),
        ([1], [2, 3, 4, 5, 6], 3.5),
        ([3], [2, 3, 4, 5, 6], 3.5),
        ([4], [2, 3, 4, 5, 6], 4),
        ([5], [2, 3, 4, 5, 6], 4.5),
        ([1, 2], [3, 4], 2.5),
        ([-1, 3], [1, 2], 1.5),
        ([1, 2], [-1, 3], 1.5),
        ([1, 4], [2, 3], 2.5),
        ([2, 3], [1, 4], 2.5),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9], 5),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9], 5),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9], 5),
        ([1, 2, 6, 7], [3, 4, 5, 8], 4.5),
    ],
)
def test_find_median_of_two_sorted_arrays(
    nums1: List[int], nums2: List[int], expected: float
) -> None:
    assert median_of_two_sorted_arrays(nums1, nums2) == expected
