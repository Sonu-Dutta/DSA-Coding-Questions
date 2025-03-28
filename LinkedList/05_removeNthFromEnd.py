class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    first = second = dummy
    for _ in range(n + 1):
        first = first.next
    while first:
        first, second = first.next, second.next
    second.next = second.next.next
    return dummy.next


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


n = 2
head = removeNthFromEnd(head, n)

print("Linked List after removing {}th node from end:".format(n))
printList(head)
