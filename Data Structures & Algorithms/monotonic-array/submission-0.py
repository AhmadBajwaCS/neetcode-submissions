class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        prev = 0

        inc = True
        dec = True

        for i, n in enumerate(nums):
            if i == 0:
                prev = n
                continue
            
            if n > prev:
                dec = False
            
            if n < prev:
                inc = False
            
            prev = n
        
        return (inc or dec)