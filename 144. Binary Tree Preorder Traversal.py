class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder_list = []

        def pre(root):
            if not root:
                return preorder_list

            preorder_list.append(root.val)
            
            if root.left:
                pre(root.left)
            if root.right:
                pre(root.right)

        pre(root)
        return preorder_list
