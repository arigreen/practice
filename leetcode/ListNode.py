from typing import Any
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional[ListNode] = None

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next


def list_node_from_list(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    head.next = list_node_from_list(lst[1:])
    return head
