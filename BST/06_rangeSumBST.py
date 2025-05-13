from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0

        def inorder(node):
            if not node:
                return

            if node.val > low:
                inorder(node.left)

            if low <= node.val <= high:
                self.total += node.val

            if node.val < high:
                inorder(node.right)

        inorder(root)
        return self.total


obj = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
low = 7
high = 15
print(obj.rangeSumBST(root, low, high))  # Output: 32
