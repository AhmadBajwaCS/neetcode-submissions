class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # for each g[i] i need to give it the lowest possible cookie above that range
        # let's sort take two pointers

        if len(s) <= 0 or len(g) <= 0:
            return 0

        greeds = sorted(g)
        sizes = sorted(s)

        #print(f"{greeds=} & {sizes=}")
    
        child_ptr = 0
        cookie_ptr = 0

        # for each child, find the next cookie that satisfies
        # so you have to basically search the cookie list until you find for each child
        # so end condition for loop would be to either have each child accounted for, 

        count = 0

        while(count < len(g) and cookie_ptr < len(s)):

            if greeds[child_ptr] <= sizes[cookie_ptr]:
                #print(f"greeds[{child_ptr}] eats sizes[{cookie_ptr}]")
                count += 1
                child_ptr += 1
                cookie_ptr += 1
            else:
                cookie_ptr += 1
        
        return count



                

        