class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif x == 0:
            return x
        else:
            ans = self.rec(x, abs(n))
            if n < 0:
                return 1/ans
            else:
                return ans
        
    def rec(self, x, n):
        if n == 1:
            return float(x)
        else:
            val = self.rec(x,n//2)
            if n%2 == 0:
                rem = 1
            else: 
                rem = x
            return rem * val * val
            
