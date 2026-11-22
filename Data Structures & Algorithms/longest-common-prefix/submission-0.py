class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        i = 0
        min_len = float("inf")
        for string in strs:
            min_len = min(len(string), min_len)
            
        res = ""

        for i in range(0, min_len):
            
            curr = strs[0][i]
        
            for string in strs[1:]:

                if string[i] != curr:
                    return res
                    break
                
                
            res += curr
        
        return res
                
                