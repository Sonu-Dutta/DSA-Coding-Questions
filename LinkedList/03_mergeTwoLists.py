class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    res = ListNode()
    if list1 == None:
        return list2
    if list2 == None:
        return list1

    if list1.val < list2.val:
        res = list1
        res.next = mergeTwoLists(list1.next, list2)

    else:
        res = list2
        res.next = mergeTwoLists(list1, list2.next)
    return res


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)


l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)


print("Merged Linked List:")
printList(mergeTwoLists(l1, l2))
