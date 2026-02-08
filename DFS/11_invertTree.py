from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# -------------------
# Example tests (VS Code)
# -------------------
if __name__ == "__main__":
    # Example 1: [1,2,2,3,4,4,3] -> True
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)

    sol = Solution()
    inverted_root = sol.invertTree(root1)

    print("Root:", inverted_root.val)
    print("Left child:", inverted_root.left.val)
    print("Right child:", inverted_root.right.val)
    print("Left-Left child:", inverted_root.left.left.val)
    print("Left-Right child:", inverted_root.left.right.val)
    print("Right-Left child:", inverted_root.right.left.val)
    print("Right-Right child:", inverted_root.right.right.val)
