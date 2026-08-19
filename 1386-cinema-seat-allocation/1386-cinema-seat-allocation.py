from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_reservations = defaultdict(set)
        for r, s in reservedSeats:
            row_reservations[r].add(s)
            
        total_groups = 2 * (n - len(row_reservations))
        
        for r, seats in row_reservations.items():
            left_free = not any(seat in seats for seat in [2, 3, 4, 5])
            right_free = not any(seat in seats for seat in [6, 7, 8, 9])
            middle_free = not any(seat in seats for seat in [4, 5, 6, 7])
            
            if left_free and right_free:
                total_groups += 2
            elif left_free or right_free or middle_free:
                total_groups += 1
                
        return total_groups