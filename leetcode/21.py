# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
from typing import cast
from typing import List
from typing import Optional

from ListNode import list_node_from_list
from ListNode import ListNode
from utils import timing


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return self.mergeTwoListsRecursive(l1, l2)

    def mergeTwoListsRecursive(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            head = ListNode(l1.val)
            rest = self.mergeTwoLists(l1.next, l2)
        else:
            head = ListNode(l2.val)
            rest = self.mergeTwoLists(l1, l2.next)
        head.next = rest
        return head

    def mergeTwoListsInline(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        else:
            current.next = l2
        return dummy.next


try:
    import pytest

    @pytest.mark.parametrize(
        ("lst1", "lst2", "expected"), [([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),]
    )
    def testMergeTwoLists(
        lst1: List[int], lst2: List[int], expected: List[int]
    ) -> None:
        assert lst1 == sorted(lst1)
        assert lst2 == sorted(lst2)
        list_node_1 = cast(ListNode, list_node_from_list(lst1))
        list_node_2 = cast(ListNode, list_node_from_list(lst2))
        expected_list_node = cast(ListNode, list_node_from_list(expected))
        with timing(f"recursive"):
            assert (
                Solution().mergeTwoListsRecursive(list_node_1, list_node_2)
                == expected_list_node
            )
        with timing(f"inline"):
            assert (
                Solution().mergeTwoListsInline(list_node_1, list_node_2)
                == expected_list_node
            )


except ModuleNotFoundError:
    pass
