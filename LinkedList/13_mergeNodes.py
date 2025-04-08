class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeNodes(head):
    head = head.next
    if head is None:
        return None
    temp = head
    sum = 0
    while (temp is not None and temp.val != 0):
        sum += temp.val
        temp = temp.next
    head.val = sum
    head.next = mergeNodes(temp)
    return head


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = ListNode(0)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(0)

print("Before:")
printList(head)

head = mergeNodes(head)
print("After:")
printList(head)
