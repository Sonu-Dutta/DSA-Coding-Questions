from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to node before `left`
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        # Reverse sublist
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next


# -------- Helper functions --------

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_linked_list(head: Optional[ListNode]) -> None:
    curr = head
    result = []
    while curr:
        result.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(result))


# -------- Main (run this) --------

if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    left, right = 2, 4

    print("Original list:")
    print_linked_list(head)

    sol = Solution()
    new_head = sol.reverseBetween(head, left, right)

    print("\nReversed list:")
    print_linked_list(new_head)
