class Solution:
    def reverseList(self, head):
        if not head:
            return head

        temp = head
        node_list = []

        while temp:
            node_list.append(temp)
            temp = temp.next
        node_list[0].next = None

        for idx, node in enumerate(node_list[1:]):
            node.next = node_list[idx]

        return node_list[-1]
