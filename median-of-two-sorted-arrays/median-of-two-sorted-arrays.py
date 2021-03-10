class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        
        out = []
        
        mid = (n + m) // 2
        
        isEven = False
        if (n + m) % 2 == 0:
            isEven = True
        
        p1 = 0
        p2 = 0
        
        count = 0
        while p1 < n or p2 < m:
            num1 = nums1[p1] if p1 < n else float('inf')
            num2 = nums2[p2] if p2 < m else float('inf')
             
            if count == mid:
                num_to_choose = min(num1, num2)
                if not isEven:
                    return num_to_choose
                else:
                    return (out[-1] + num_to_choose) / 2
            
            count += 1
            
            if num1 < num2:
                p1 += 1
                out.append(num1)
            else:
                p2 += 1
                out.append(num2)
        
        return -1
            