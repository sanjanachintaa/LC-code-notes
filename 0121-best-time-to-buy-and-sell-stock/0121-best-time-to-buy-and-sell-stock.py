class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        max_profit,max1=0,0
        while r<len(prices):
            if prices[l]<prices[r]:
                max1=prices[r]-prices[l]
                r+=1
            else:
                l=r
                r+=1
            max_profit=max(max_profit,max1)
        return max_profit
        