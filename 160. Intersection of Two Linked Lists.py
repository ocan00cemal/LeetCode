class Solution:
    def getIntersectionNode(self, headA, headB):
        temp_a = headA
        temp_b = headB
        node_dict = {}

        while temp_a:
            node_dict[temp_a] = True
            temp_a = temp_a.next

        while temp_b:
            try:
                if node_dict[temp_b]:
                    return temp_b
            except:
                temp_b = temp_b.next
        return None
