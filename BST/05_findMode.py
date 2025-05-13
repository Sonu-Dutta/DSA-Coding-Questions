from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.modes = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1
                self.prev = node.val

            if self.count > self.max_count:
                self.max_count = self.count
                self.modes = [node.val]
            elif self.count == self.max_count:
                self.modes.append(node.val)

            inorder(node.right)

        inorder(root)
        return self.modes


obj = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)
root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(3)

print(obj.findMode(root))
