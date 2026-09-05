class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        pref_max = [0] * n
        current_max = -float('inf')
        for i in range(n):
            current_max = max(current_max, nums[i])
            pref_max[i] = current_max
            
        suff_min = [0] * n
        current_min = float('inf')
        for i in range(n - 1, -1, -1):
            current_min = min(current_min, nums[i])
            suff_min[i] = current_min
            
        for i in range(n):
            if pref_max[i] - suff_min[i] <= k:
                return i
                
        return -1