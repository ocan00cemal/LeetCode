class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:

        if root.val == x or root.val == y:
            return False

        cousins = [[x, 0, 0], [y, 0, 0]]

        def backtrack(root, depth=0, parent_val=root.val):

            if root.val == x:
                cousins[0][1] = depth
                cousins[0][2] = parent_val
            elif root.val == y:
                cousins[1][1] = depth
                cousins[1][2] = parent_val

            if root.left:
                backtrack(root.left, depth + 1, root.val)
            if root.right:
                backtrack(root.right, depth + 1, root.val)

        backtrack(root)
        if cousins[0][1] == 0:
            return False
        return cousins[0][1] == cousins[1][1] and not cousins[0][2] == cousins[1][2]
