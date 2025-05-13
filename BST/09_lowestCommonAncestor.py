class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


# Example usage
obj = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
p = root.left
q = root.right
lca = obj.lowestCommonAncestor(root, p, q)
print(lca.val)

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root is None:
#             return None
#         if root==p or root==q:
#             return root

#         right=self.lowestCommonAncestor(root.right, p,q)
#         left=self.lowestCommonAncestor(root.left, p, q)

#         if left and right:
#             return root

#         if right is None:
#             return left

#         if left is None:
#             return right
