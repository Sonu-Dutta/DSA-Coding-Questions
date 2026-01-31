from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )


# -------------------
# Example tests (VS Code)
# -------------------
if __name__ == "__main__":
    # Tree 1: [1,2,3]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    # Tree 2: [1,2,3]
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    sol = Solution()
    print(sol.isSameTree(p, q))  # Expected output: True

    # Tree 3: [1, None, 2]
    r = TreeNode(1)
    r.right = TreeNode(2)

    print(sol.isSameTree(p, r))  # Expected output: False
