class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        pref_max = [0] * n
        curr_max = -float('inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            pref_max[i] = curr_max
            
        suff_min = [0] * n
        curr_min = float('inf')
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suff_min[i] = curr_min
            
        for i in range(n):
            if pref_max[i] - suff_min[i] <= k:
                return i
                
        return -1 