# 11. Container With Most Water
# Given n non-negative integers a1, a2, ..., an, where each represents a point at
# coordinate (i, ai), n vertical lines are drawn such that the two endpoints of line i
# is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container,
# such that the container contains the most water.
# Note: You may not slant the container and n is at least 2
from typing import List


def max_area_naive(height: List[int]) -> int:
    # For each possible start and end point, find the area,
    # and return the max
    def area(i: int, j: int) -> int:
        # Assumes i < j
        return min(height[i], height[j]) * (j - i)

    max = 0
    size = len(height)
    for i in range(size):
        for j in range(i + 1, size):
            if area(i, j) > max:
                max = area(i, j)
    return max


def max_area_faster(height: List[int]) -> int:
    def area(i: int, j: int) -> int:
        # Assumes i < j
        return min(height[i], height[j]) * (j - i)

    max = 0
    size = len(height)
    for i in range(size):
        if i > 0 and height[i] <= height[i - 1]:
            continue
        for j in range(size - 1, i, -1):
            a = area(i, j)
            if a > max:
                max = a
            if height[j] >= height[i]:
                break
    return max


def max_area_two_pointers(height: List[int]) -> int:
    # Maintain a left pointer, a right pointer, and the current max
    # Invariant: The global max is either the current max, or within the bounds
    # of the 2 pointers

    def area(i: int, j: int) -> int:
        # Assumes i < j
        return min(height[i], height[j]) * (j - i)

    left = 0
    right = len(height) - 1
    current_max = area(left, right)

    while left < right:
        if height[left] < height[right]:
            a = area(left + 1, right)
            left += 1
        else:
            a = area(left, right - 1)
            right -= 1
        if a > current_max:
            current_max = a

    return current_max


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return max_area_two_pointers(height)


try:
    import pytest

    @pytest.mark.parametrize(
        ("height", "expected"), [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),],
    )
    def test_max_area(height: List[int], expected: int) -> None:
        assert max_area_naive(height) == expected
        assert max_area_two_pointers(height) == expected


except ModuleNotFoundError:
    pass
