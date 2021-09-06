# 99.30 / 63.70
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        elif n == 2:
            return max(prices[1]-prices[0], 0)
                
        profits = [-prices[0],0,0] #[[buy, sell, cooldown]]
        
        '''
        buy = can only be done after a cooldown before,
        sell = can only be done when something is already bought
        '''
        
        for i in range(1, n):
            price = prices[i]
            b,s,c = profits
            
            profits = [max(b,c-price), b+price, max(s,c)]
            
        return max(profits[1], profits[2])
