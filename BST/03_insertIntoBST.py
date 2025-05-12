from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


# Example usage:
if __name__ == "__main__":
    # Constructing a BST
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    val = 5

    solution = Solution()
    new_root = solution.insertIntoBST(root, val)

    # Function to print the inorder traversal of the BST
    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val, end=' ')
            inorder(node.right)

    # Print the updated BST
    inorder(new_root)  # Output: 1 2 3 4 5 7
    print()
