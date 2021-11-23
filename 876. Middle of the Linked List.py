class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_dict = {}
        temp = head
        i = 1

        while temp:
            node_dict[i] = temp
            temp = temp.next
            i = i + 1

        if i % 2 == 0:
            return node_dict[i // 2]
        else:
            return node_dict[i // 2 + 1]
