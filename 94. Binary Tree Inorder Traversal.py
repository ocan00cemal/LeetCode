class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]):
        
        if not root:
            return []
        
        num_list = []
        
        if root.left:   
            num_list += self.inorderTraversal(root.left)
        
        num_list.append(root.val)
            
        if root.right:
         
            num_list += self.inorderTraversal(root.right)
        
        return num_list