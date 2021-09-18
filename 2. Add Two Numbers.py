# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = cur = ListNode(0)
        increase = 0

        while l1 != None and l2 != None:
            if l1.val + l2.val + increase >= 10:
                cur.next = ListNode((l1.val + l2.val + increase) % 10)
                increase = 1
            else:
                cur.next = ListNode(l1.val + l2.val + increase)
                increase = 0

            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        if l1 != None or l2 != None:
            l_remain = l1 or l2
            while l_remain != None:
                if l_remain.val + increase >= 10:
                    cur.next = ListNode((l_remain.val + increase) % 10)
                    increase = 1
                else:
                    cur.next = ListNode(l_remain.val + increase)
                    increase = 0

                l_remain = l_remain.next
                cur = cur.next

        if increase:
            cur.next = ListNode(increase)

        return head.next
