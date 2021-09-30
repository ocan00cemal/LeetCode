class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head

        temp = head
        num_list = [head.val]

        while temp.next:
            if temp.next.val in num_list:
                temp.next = temp.next.next
            else:
                num_list.append(temp.next.val)
                temp = temp.next

        return head
