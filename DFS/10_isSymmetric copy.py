from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return (
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left)
            )

        return isMirror(root.left, root.right)


# -------------------
# Example tests (VS Code)
# -------------------
if __name__ == "__main__":
    # Example 1: [1,2,2,3,4,4,3] -> True
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    sol = Solution()
    print(sol.isSymmetric(root1))  # Expected: True

    # Example 2: [1,2,2,None,3,None,3] -> False
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)

    print(sol.isSymmetric(root2))  # Expected: False
