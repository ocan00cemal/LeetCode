class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        post_list = []
       
        def pre(root):
            if not root:
                return post_list          
            if root.left:
                pre(root.left)
            if root.right:
                pre(root.right)
            post_list.append(root.val)
       
        pre(root)
        return post_list