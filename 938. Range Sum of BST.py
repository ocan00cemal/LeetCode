class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result_list = []

        def backtrack(head):
            if head.val >= low and head.val <= high:
                result_list.append(head.val)
            if head.left:
                backtrack(head.left)
            if head.right:
                backtrack(head.right)

        backtrack(root)
        return sum(result_list)
