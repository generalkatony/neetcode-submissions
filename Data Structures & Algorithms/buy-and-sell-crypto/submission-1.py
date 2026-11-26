class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        r = 0
        while r < len(prices):  
            if prices[l] <= prices[r]:
                maxProfit = max(maxProfit,(prices[r]-prices[l]))
                r += 1
            else:
                l += 1

        return maxProfit