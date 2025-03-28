class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


print("Original Linked List:")
printList(head)

reversed_head = reverseList(head)

print("Reversed Linked List:")
printList(reversed_head)
