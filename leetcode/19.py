# 19. Remove Nth Node From End of List
# Given a linked list, remove the n-th node from the end of list and return its head.
# Note: Given n will always be valid.
from typing import cast
from typing import List
from typing import Optional

from ListNode import list_node_from_list
from ListNode import ListNode
from utils import timing


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        if not head:
            return head

        trailing: Optional[ListNode] = head
        assert trailing
        leading: Optional[ListNode] = head

        # Advance back N places
        for _ in range(n):
            if leading:
                leading = leading.next

        if not leading:
            return head.next

        while leading.next:
            trailing = trailing.next
            assert trailing
            leading = leading.next

        if trailing.next:
            assert trailing.next
            trailing.next = trailing.next.next

        return head


try:
    import pytest

    @pytest.mark.parametrize(
        ("lst", "n", "expected"), [([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),]
    )
    def testRemoveNthFromEnd(lst: List[int], n: int, expected: List[int]) -> None:
        with timing(f"test"):
            list_node = cast(ListNode, list_node_from_list(lst))
            expected_list_node = cast(ListNode, list_node_from_list(expected))
            assert Solution().removeNthFromEnd(list_node, n) == expected_list_node


except ModuleNotFoundError:
    pass
