class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    curr = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            curr = curr.next
            list1 = list1.next
        else:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
    if list1 or list2:
        if list1:
            curr.next = list1
        else:
            curr.next = list2
    return dummy.next


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
