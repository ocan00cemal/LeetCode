class Solution:
    def hasCycle(self, head) -> bool:
        if head == None:
            return False

        temp = head
        node_list = []

        while temp.next:

            if temp in node_list:
                return True
            else:
                node_list.append(temp)
                temp = temp.next

        return False
