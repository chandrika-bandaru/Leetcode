from collections import Counter
import math

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = Counter(nums)
        ans = 1
        
        if count[1] > 0:
            if count[1] % 2 == 0:
                ans = max(ans, count[1] - 1)
            else:
                ans = max(ans, count[1])
        for x in count:
            if x == 1:
                continue
            
            curr = x
            length = 0
            
            while curr in count:
                if count[curr] >= 2:
                    length += 2
                    curr = curr * curr
                else:
                    length += 1
                    break
            if length % 2 == 0:
                length -= 1
                
            ans = max(ans, length)
            
        return ans