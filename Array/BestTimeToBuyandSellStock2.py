class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        hold = False
        minPrice = 99999
        maxPrice = 0
        for i in range(len(prices)):
            #print(hold,profit, prices[i],minPrice,maxPrice)
            if not hold: #does not have a stock
                if prices[i] <= minPrice:
                    minPrice = prices[i]
                else:
                    #buy the minPrice stock
                    profit -= minPrice
                    maxPrice = prices[i]
                    minPrice = 99999
                    hold = True
            else: #hold a stock
                if prices[i] >= maxPrice:
                    maxPrice = prices[i]
                    if i == len(prices)-1:
                        profit += maxPrice
                        hold = False
                else: 
                    #sell the maxPrice stock
                    profit += maxPrice
                    maxPrice = 0
                    minPrice = prices[i]
                    hold = False
        if hold:
            profit += prices[-1]
        return profit
                
