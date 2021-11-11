class Solution:
    def isSymmetric(self, root) -> bool:
   
        if not root.left and not root.right:
            return True
        if not root.left and root.right:
            return False
        if root.left and not root.right:
            return False
        
        root_left = root.left
        root_right = root.right   
        left_list = []
        right_list = []
        
        
        def search_left(root_l, l_l):
            if root_l.left:
                l_l.append("left")
                search_left(root_l.left, l_l)
            
            l_l.append(root_l.val)
            
            if root_l.right:
                l_l.append("right")
                search_left(root_l.right, l_l)
                  
        def search_right(root_r, r_l):
            if root_r.right:
                r_l.append("right")
                search_right(root_r.right, r_l)
                
            r_l.append(root_r.val)
            
            if root_r.left:
                r_l.append("left")
                search_right(root_r.left, r_l)
        
        search_left(root_left, left_list)
        search_right(root_right, right_list)
        
        for i, ele in enumerate(right_list):
            if ele == "left":
                right_list[i] = "right"
            elif ele == "right":
                right_list[i] = "left"
        
            
        if left_list == right_list:
            return True
        else:
            return False