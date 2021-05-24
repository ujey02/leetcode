class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
            
        if (dividend == 2**31 - 1 and divisor == 1) or (dividend == -2**31 and divisor == -1):
            return 2**31-1
        elif (dividend == -2**31 and divisor == 1):
            return -2**31
        
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        ans = 0
        self.stack = divisor
        
        while dividend >= divisor:
                ans += self.divide2(dividend-divisor)
                dividend -= self.stack
                self.stack = divisor
        
        if sign < 0:
            return 0 - ans
        
        return ans
        
    def divide2(self, dividend):
        count = 1
        
        while True:
            dividend -= self.stack
            if dividend < 0:
                return count
            else:
                count += count
                self.stack += self.stack
        
        return count

        
        
        
        
