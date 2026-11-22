class Solution:
    def hammingWeight(self, n: int) -> int:
        
        binary = f"{n:b}"
        count = 0
        #print(binary)
        for c in binary:
            if c == "1":
                count += 1

        return count