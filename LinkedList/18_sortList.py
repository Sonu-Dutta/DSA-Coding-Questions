from typing import Optional, List

# Definition for singly-linked list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Split the list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge sorted halves
        return self.merge(left, right)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next


# ---------- Helper functions for VS Code ----------

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def print_linked_list(head: Optional[ListNode]):
    if not head:
        print("None")
        return
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) + " -> None")


# ---------- Run examples ----------

if __name__ == "__main__":
    sol = Solution()

    head1 = build_linked_list([4, 2, 1, 3])
    print("Example 1:")
    print_linked_list(sol.sortList(head1))

    head2 = build_linked_list([-1, 5, 3, 4, 0])
    print("\nExample 2:")
    print_linked_list(sol.sortList(head2))

    head3 = build_linked_list([])
    print("\nExample 3:")
    print_linked_list(sol.sortList(head3))
