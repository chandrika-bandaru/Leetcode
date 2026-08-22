class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        
        digit_sum = 0
        digit_product = 1
        
        for char in s:
            digit = int(char)
            digit_sum += digit
            digit_product *= digit
            
        total_divisor = digit_sum + digit_product
        
        return n % total_divisor == 0 if total_divisor != 0 else False