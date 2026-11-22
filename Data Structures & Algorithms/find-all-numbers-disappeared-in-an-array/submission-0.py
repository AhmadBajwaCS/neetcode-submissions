class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        start = 1
        comparison = set()
        for n in nums:
            comparison.add(start)
            start+=1

        print(comparison)
        res = []
        nums_set = set(nums)

        for n in comparison:
            if n not in nums_set:
                res.append(n)
        
        return res
