class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        temp = head
        node_list = []

        while temp.next != None:
            node_list.append([temp, temp.next])
            if temp.next.next != None:
                temp = temp.next.next
            else:
                break

        if node_list[-1][1].next:
            add = True
            add_node = node_list[-1][1].next

        else:
            add = False

        for i in range(len(node_list)):
            try:
                node_list[i][0].next = node_list[i + 1][1]
                node_list[i][1].next = node_list[i][0]
            except:
                break

        node_list[-1][1].next = node_list[-1][0]

        if add:
            node_list[-1][0].next = add_node
            return node_list[0][1]
        else:
            node_list[-1][0].next = None
            return node_list[0][1]
