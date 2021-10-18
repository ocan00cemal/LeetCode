class Solution:
    def reverseList(self, head):
        global new_head

        if not head or not head.next:
            return head

        def rec(node):
            global new_head

            if not node.next:
                new_head = node
                return new_head

            rec(node.next).next = node
            return node

        rec(head)
        head.next = None

        return new_head
