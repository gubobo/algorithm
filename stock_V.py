class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length=len(prices)
        if length<2 or not prices:
            return 0
        sellP=[0 for i in range(length)]
        buyP=[0 for i in range(length)]

        buyP[0]=-prices[0]
        for i in range(1,length):
            sellP[i] = max(sellP[i-1] , buyP[i-1]+prices[i])
            if i>=2:
                buyP[i]=max(buyP[i-1],sellP[i-2]-prices[i])
            else:
                buyP[i] = max(buyP[i-1],-prices[i])

        return sellP[length-1]

prices = [1,2,4]
a = Solution()
b = a.maxProfit(prices)
print b