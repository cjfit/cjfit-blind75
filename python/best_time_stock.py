# Naive Implementation - Bruteforce
# Not recommended - O(n)^2 runtime
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stocks = {}
        max_profit = 0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)-1):
                if prices[j] > prices[i] and prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
                    
        return(max_profit)
            
