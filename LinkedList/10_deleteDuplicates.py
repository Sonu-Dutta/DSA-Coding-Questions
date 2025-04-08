class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    res = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return res


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)


print("Before:")
printList(head)

deleteDuplicates(head)
print("After:")
printList(head)
