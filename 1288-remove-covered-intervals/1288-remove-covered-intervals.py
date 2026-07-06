class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        active_end = 0
        
        for _, end in intervals:
            if end > active_end:
                count += 1
                active_end = end
                
        return count