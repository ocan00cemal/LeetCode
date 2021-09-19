class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = temp = ListNode(0)
        increase = 0

        while l1 != None and l2 != None:
            if l1.val + l2.val + increase >= 10:
                temp.next = ListNode((l1.val + l2.val + increase) % 10)
                increase = 1

            else:
                temp.next = ListNode(l1.val + l2.val + increase)
                increase = 0

            l1 = l1.next
            l2 = l2.next

            temp = temp.next

        if l1 != None or l2 != None:
            l_remain = l1 or l2
            while l_remain != None:
                if l_remain.val + increase >= 10:
                    temp.next = ListNode((l_remain.val + increase) % 10)
                    increase = 1

                else:
                    temp.next = ListNode(l_remain.val + increase)
                    increase = 0

                l_remain = l_remain.next
                temp = temp.next

        if increase:
            temp.next = ListNode(increase)

        return head.next
