class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # repeating pattern

        max_len = len(str1)
        divisor = len(str2)

        operations = max_len // divisor

        res = ""
        ptr = 0


        factors = []

        def get_factors(string):
            n = len(string)
            factors = []
            for i in range(1, len(string)):
                #print()
                factor = string[0:i]    
                factor_len = len(factor)

                ops = len(string) // factor_len

                #print(f"{curr=}, {ops=}, {len(str1)=} // {curr_len=}")
                
                if (len(string) % factor_len != 0):
                    continue
                
                curr = factor * ops
                

                #print(f"testing {factor=}")
                if curr != string:
                    continue
                
                factors.append(factor)
            factors.append(string)
            return factors

            #print(f"{factors=}")

        str1_factors = get_factors(str1)
        str2_factors = get_factors(str2)

        str2_fctr_set = set(str2_factors)
        for factor in str1_factors:
            if factor in str2_factors:
                res = factor

        #print(f"{str1_factors=} & {str2_factors=}")

        return res

        

        #ABAB
        #ATWE       

        