from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


# ---------- Helper Functions (for testing) ----------

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------- Run Example Tests ----------

if __name__ == "__main__":
    sol = Solution()

    head1 = build_linked_list([1, 2, 3, 4, 5])
    result1 = sol.oddEvenList(head1)
    print(linked_list_to_list(result1))  # [1, 3, 5, 2, 4]

    head2 = build_linked_list([2, 1, 3, 5, 6, 4, 7])
    result2 = sol.oddEvenList(head2)
    print(linked_list_to_list(result2))  # [2, 3, 6, 7, 1, 5, 4]
