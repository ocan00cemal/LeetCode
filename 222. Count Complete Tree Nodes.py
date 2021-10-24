class Solution:
    def countNodes(self, root) -> int:
        global counter
        counter = 0

        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        def backtrack(root):
            global counter
            counter += 1

            if root.left:
                backtrack(root.left)
            if root.right:
                backtrack(root.right)

        backtrack(root)
        return counter
