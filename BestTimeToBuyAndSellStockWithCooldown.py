# 99.30 / 63.70
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(prices[1]-prices[0], 0)
        
        profits = [-prices[0],0,-1001,-1001] #[[buy, sell, buy-cooldown, sell-cooldown]]
        
        '''
        buy = can only be done when previous action is sell-cooldown,
        sell = can only be done when previous action is buy or buy-cooldown
        '''
        
        for i in range(1,len(prices)):
            price = prices[i]
            b,s,bc,sc = profits
            bb = max(b, bc)
            
            profits = [max(-price,sc-price), bb+price, bb, max(s,sc)]
        
        # print (profits)
        return max(profits[1], profits[3])
