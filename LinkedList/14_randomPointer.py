# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {None: None}
        curr = head
        while curr:
            newNode = Node(curr.val)
            mapping[curr] = newNode
            curr = curr.next

        curr = head
        while curr:
            newNode = mapping[curr]
            newNode.next = mapping[curr.next]
            newNode.random = mapping[curr.random]
            curr = curr.next

        return mapping[head]


# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         # If the original list is empty, return None
#         if not head:
#             return None

#         # Step 1: Clone each node and insert the copy right after the original node
#         curr = head
#         while curr:
#             newNode = Node(curr.val)
#             newNode.next = curr.next
#             curr.next = newNode
#             curr = newNode.next

#         # Step 2: Assign random pointers to the copied nodes
#         curr = head
#         while curr:
#             if curr.random:
#                 # curr.next is the copied node, curr.random.next is the copy of curr.random
#                 curr.next.random = curr.random.next
#             curr = curr.next.next  # Move to the next original node

#         # Step 3: Separate the original list and the copied list
#         curr = head
#         newHead = head.next  # Head of the copied list
#         newCurr = newHead
#         while curr:
#             curr.next = newCurr.next  # Restore the original list
#             curr = curr.next
#             if curr:
#                 newCurr.next = curr.next  # Link copied nodes
#                 newCurr = newCurr.next

#         # Return the head of the deep-copied list
#         return newHead

#         # Example usage


def printList(head: Optional[Node]):
    while head:
        random_val = head.random.val if head.random else None
        print(f"Node({head.val}, Random({random_val}))", end=" -> ")
        head = head.next
    print("None")


# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.random = head.next  # Node 1's random points to Node 2
head.next.random = head  # Node 2's random points to Node 1
head.next.next.random = head  # Node 3's random points to Node 1
print("Before:")
printList(head)
solution = Solution()
copied_head = solution.copyRandomList(head)
print("After:")
# Should print the copied list with correct random pointers
printList(copied_head)
