class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        while head.val == val:
            head = head.next
            if not head:
                return head
            
        left = head
        right = left.next
        
        while right:
            if right.val == val:
                right = right.next
                left.next = right
            else:
                left = left.next
                right = right.next
        
        return head