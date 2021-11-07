class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        i = 0
        while nums2 and i < len(nums1):
            if nums2[0] <= nums1[i]:
                nums1.insert(i, nums2[0])
                nums1.pop()
                del nums2[0]       
            i += 1
    
        for i in range(len(nums2)):
            nums1.pop()
        for i in range(len(nums2)):
            nums1.append(nums2[0])
            del nums2[0]
            
        return nums1
