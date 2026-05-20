class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return []
        res = []
        
        # Track the index (i) and the value (n) of the current element
        for i, n in enumerate(nums):  
            temp = 1
            # Track the index (j) and value (num) of the other elements
            for j, num in enumerate(nums):
                # FIX: Skip ONLY if it's the exact same position in the array
                if i != j:
                    temp *= num
            res.append(temp)
        return res
                
