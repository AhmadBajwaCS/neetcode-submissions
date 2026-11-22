class Solution:
    def encode(self, strs: List[str]) -> str:
        # le
        if len(strs) == 0:
            return ""

        prefix = ""
        postfix = ""
        for i, s in enumerate(strs):
            length = len(s)
            prefix = prefix + str(length)

            
            if i < (len(strs) -1):
                prefix += "_"

            postfix = postfix + s

        encoded_str = prefix + "." + postfix
        #print(encoded_str)

        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        decoded_strs = []

        period_ind = s.find(".")
        decoded = [s[0:period_ind], s[period_ind+1:]]
        decoded_prefix = decoded[0].split("_")
        decoded_postfix = decoded[1]

        i = 0
        for length in decoded_prefix:
            j = (i + int(length))
            decoded_strs.append(decoded_postfix[i:j])
            i = j

        #print(decoded)
        #print(decoded_prefix)
        
        return decoded_strs
