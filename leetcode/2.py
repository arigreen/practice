# Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
from typing import Optional

import pytest


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x: int) -> None:
        self.val = x
        self.next: Optional[ListNode] = None


def num_to_list(num: int) -> ListNode:
    if num < 0:
        raise Exception(f"Invalid number {num}")

    if num < 10:
        return ListNode(num)

    ones_digit = num % 10
    rest = num // 10
    lst = ListNode(ones_digit)
    lst.next = num_to_list(rest)
    return lst


def list_to_num(lst: ListNode) -> int:
    result = 0
    multiplier = 1
    current: Optional[ListNode] = lst
    while current:
        result += multiplier * current.val
        current = current.next
        multiplier *= 10

    return result


def add_two_numbers(list1: ListNode, list2: ListNode) -> ListNode:
    return num_to_list(list_to_num(list1) + list_to_num(list2))


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return add_two_numbers(l1, l2)


def test_helpers() -> None:
    for num in range(1000):
        assert list_to_num(num_to_list(num)) == num


@pytest.mark.parametrize(("num1", "num2"), [(243, 564), (0, 0), (1, 2)])
def test_add_two_numbers(num1: int, num2: int) -> None:
    assert (
        list_to_num(add_two_numbers(num_to_list(num1), num_to_list(num2)))
        == num1 + num2
    )
