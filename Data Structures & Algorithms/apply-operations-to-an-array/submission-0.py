class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        for n in nums:
            if n != 0:
                res.append(n)
        
        while len(res) < len(nums):
            res.append(0)

        return res
