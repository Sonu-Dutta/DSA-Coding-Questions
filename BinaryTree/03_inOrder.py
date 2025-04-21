
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrder(self, root: TreeNode):
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res


#         1
#        / \
#       2   3
#      / \
#     4   5
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

sol = Solution()
print(sol.inOrder(root))
