class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        binary = ""
        
        while temp:
            binary = binary + str(temp.val)
            temp = temp.next

        return int(binary, 2)