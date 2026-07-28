from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        
        first_half = []
        middle_char = ""
        
        for char in sorted(count.keys()):
            freq = count[char]
            first_half.append(char * (freq // 2))
            
            if freq % 2 == 1:
                middle_char = char
                
        left_part = "".join(first_half)
        
        return left_part + middle_char + left_part[::-1]