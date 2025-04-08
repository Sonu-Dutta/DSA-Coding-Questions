class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA, headB):
    currA, currB = headA, headB

    while currA != currB:
        if currA is None:
            currA = headB
        else:
            currA = currA.next

        if currB is None:
            currB = headA
        else:
            currB = currB.next
    return currA


head = ListNode(1)
# Create List A: 1 -> 2 -> 3 -> 4 -> 5
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

# Create List B: 9 -> 8 -> (intersect at 4 from List A)
headB = ListNode(9)
headB.next = ListNode(8)

headB.next.next = headA.next.next.next

intersection = getIntersectionNode(headA, headB)
if intersection:
    print(f"Intersection at node with value: {intersection.val}")
else:
    print("No intersection")
