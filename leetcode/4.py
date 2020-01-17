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
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    if len(nums1) == 0:
        return median(nums2)

    elif len(nums1) == 1:
        if len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2
        median_of_2 = median(nums2)
        if nums1[0] == median_of_2:
            return nums1[0]
        elif nums1[0] < median_of_2:
            return median_of_two_sorted_arrays([], nums2[:-1])
        else:
            return median_of_two_sorted_arrays([], nums2[1:])
    else:
        num_to_remove = len(nums1) // 2
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
        ([1], [2], 1.5),
        ([1, 3], [2], 2),
        ([1, 2], [3], 2),
        ([1], [2, 3, 4, 5, 6], 3.5),
        ([3], [2, 3, 4, 5, 6], 3.5),
        ([4], [2, 3, 4, 5, 6], 4),
        ([5], [2, 3, 4, 5, 6], 4.5),
        ([1, 2], [3, 4], 2.5),
        ([1, 4], [2, 3], 2.5),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9], 5),
    ],
)
def test_find_median_of_two_sorted_arrays(
    nums1: List[int], nums2: List[int], expected: float
) -> None:
    assert median_of_two_sorted_arrays(nums1, nums2) == expected
