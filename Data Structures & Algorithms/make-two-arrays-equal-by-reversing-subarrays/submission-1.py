class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        

        freq_target = {}
        freq_arr = {}

        for n in target:
            freq_target[n] = freq_target.get(n, 0) + 1
        
        for n in arr:
            freq_arr[n] = freq_arr.get(n, 0) + 1

        for n in arr:
            if n not in freq_target:
                return False

            if freq_arr[n] > freq_target[n]:
                return False

        return True
