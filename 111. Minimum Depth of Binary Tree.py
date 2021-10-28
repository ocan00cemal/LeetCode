class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        global min_depth
        min_depth = pow(10, 5)

        def backtrack(root, count=1):
            global min_depth

            if not root.left and not root.right:
                if count < min_depth:
                    min_depth = count
                return

            if root.left:
                backtrack(root.left, count + 1)

            if root.right:
                backtrack(root.right, count + 1)

        backtrack(root)
        return min_depth
