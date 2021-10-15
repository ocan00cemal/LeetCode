class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0   
        if not root.left and not root.right:
            return 1   
        
        def backtrack(node, count=1, cur_max=1):           
            if node.left:             
                cur_max = backtrack(node.left, count + 1, cur_max)

            if node.right:         
                cur_max = backtrack(node.right, count + 1, cur_max)
                
            if count >= cur_max:
                    cur_max = count  
            return cur_max
 
        return backtrack(root)