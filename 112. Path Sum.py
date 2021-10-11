class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        global result
        result = False

        if not root:
            return False
        elif not root.left and not root.right:
            if root.val != targetSum:
                return False
            elif root.val == targetSum:
                return True

        def rec(root, current_total, target):
            global result

            if not root.left and not root.right and current_total == target:
                result = True

            if root.left:
                rec(root.left, current_total + root.left.val, targetSum)

            if root.right:
                rec(root.right, current_total + root.right.val, targetSum)

        rec(root, root.val, targetSum)
        return result
