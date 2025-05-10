from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))


# Example usage:
if __name__ == "__main__":
    # Constructing a valid BST
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(15)

    solution = Solution()
    print(solution.isValidBST(root))
