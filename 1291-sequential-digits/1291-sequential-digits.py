class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        s = "123456789"
        
        for length in range(2, 10):
            for i in range(len(s) - length + 1):
                num = int(s[i:i + length])
                if low <= num <= high:
                    result.append(num)
        
        return result