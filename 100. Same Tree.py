class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        p_list = []
        q_list = []

        def search(root, node_list):
            if root.left:
                node_list.append("left")
                search(root.left, node_list)

            node_list.append(root.val)

            if root.right:
                node_list.append("right")
                search(root.right, node_list)

        search(p, p_list)
        search(q, q_list)
        if p_list == q_list:
            return True
        else:
            return False
