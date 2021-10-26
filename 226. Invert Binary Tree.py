class Solution:
    def invertTree(self, root):
        if not root:
            return root

        def invert(root):
            if root.left and root.right:
                root.left, root.right = root.right, root.left
                invert(root.left)
                invert(root.right)

            elif root.left:
                root.right, root.left = root.left, None
                invert(root.right)

            elif root.right:
                root.left, root.right = root.right, None
                invert(root.left)

        invert(root)
        return root
