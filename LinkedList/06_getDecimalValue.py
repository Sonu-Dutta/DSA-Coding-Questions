class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head):
    res = 0
    while head:
        res = 2*res + head.val
        head = head.next
    return res


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

print(getDecimalValue(head))
