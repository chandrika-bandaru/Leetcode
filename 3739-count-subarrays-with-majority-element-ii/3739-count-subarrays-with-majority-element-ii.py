from typing import List

class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = [1 if x == target else -1 for x in nums]
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + arr[i]
            
        sorted_prefs = sorted(list(set(pref)))
        rank = {val: i + 1 for i, val in enumerate(sorted_prefs)}
        
        ft = FenwickTree(len(sorted_prefs))
        count = 0
        
        for p in pref:
            count += ft.query(rank[p] - 1)
            ft.update(rank[p], 1)
            
        return count