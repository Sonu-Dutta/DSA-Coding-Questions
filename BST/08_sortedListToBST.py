
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        def find_middle(start):
            prev = None
            slow = fast = start
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev:
                prev.next = None
            return slow

        if not head.next:
            return TreeNode(head.val)

        mid = find_middle(head)
        root = TreeNode(mid.val)

        if mid != head:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root


# Example usage
obj = Solution()
head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)
root = obj.sortedListToBST(head)


def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.val, end=' ')
        print_inorder(node.right)


print_inorder(root)  # Output: -10 -3 0 5 9
