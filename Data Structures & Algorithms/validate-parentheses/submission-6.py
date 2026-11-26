class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2:
            return False

        stack = []

        pairs = {
            '(': ')', '{': '}', '[' : ']'

        }

        start = True

        for c in s:

            if c in pairs:
                #opening
                stack.append(c)
            else:
                # closing
                if len(stack) == 0:
                    return False

                curr = stack.pop()
                if pairs[curr] != c:
                    return False
            start = False
        
        if len(stack) > 0:
            return False
        
        return True


        