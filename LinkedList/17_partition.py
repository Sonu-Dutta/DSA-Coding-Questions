from typing import Optional, List

# Definition for singly-linked list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(0), ListNode(0)
        leftP, rightP = left, right

        while head:
            if head.val < x:
                leftP.next = head
                leftP = leftP.next
            else:
                rightP.next = head
                rightP = rightP.next
            head = head.next

        rightP.next = None
        leftP.next = right.next

        return left.next


# ---------- Helper functions for VS Code testing ----------

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def print_linked_list(head: Optional[ListNode]):
    if not head:
        print("None")
        return
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) + " -> None")


# ---------- Run example test cases ----------

if __name__ == "__main__":
    sol = Solution()

    head1 = build_linked_list([1, 4, 3, 2, 5, 2])
    result1 = sol.partition(head1, 3)
    print("Result 1:")
    print_linked_list(result1)   # 1 → 2 → 2 → 4 → 3 → 5 → None

    head2 = build_linked_list([2, 1])
    result2 = sol.partition(head2, 2)
    print("\nResult 2:")
    print_linked_list(result2)   # 1 →
