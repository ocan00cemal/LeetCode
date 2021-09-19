class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        num_list = []

        while temp:
            num_list.append(temp.val)
            temp = temp.next

        head = None
        num_list.pop(-n)
        new_head = temp = ListNode(0)

        for i in num_list:
            temp.next = ListNode(i)
            temp = temp.next

        return new_head.next
