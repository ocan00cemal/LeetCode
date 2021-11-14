class Solution:
    def addTwoNumbers(self, l1, l2):
        head = temp = ListNode(0)
        remainder = 0

        while l1 and l2:
            if l1.val + l2.val + remainder >= 10:
                temp.next = ListNode((l1.val + l2.val + remainder) % 10)
                remainder = 1
            else:
                temp.next = ListNode(l1.val + l2.val + remainder)
                remainder = 0
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
     
        long_linked = l1 or l2

        while long_linked:
            if long_linked.val + remainder >= 10:
                temp.next = ListNode((long_linked.val + remainder) % 10)
                remainder = 1
            else:
                temp.next = ListNode(long_linked.val + remainder)
                remainder = 0
            long_linked = long_linked.next
            temp = temp.next

        if remainder:
            temp.next = ListNode(remainder)

        return head.next
