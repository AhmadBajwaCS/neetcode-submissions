class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        out = [[]]

        for n in nums:
            print("n:", n)
            subset = []
            new_subsets = []
            for curr_set in out:
                print("curr_set:", curr_set)
                subset = curr_set.copy()
                subset.append(n)
                new_subsets.append(subset)
            print("new_subsets: ", new_subsets)

            for subset in new_subsets:
                out.append(subset)
            
        return out