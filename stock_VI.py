#encoding:utf-8
import math

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        length=len(prices)

        local=[[0 for col in range(k+1)] for row in range(length)]
        glob=[[0 for col in range(k+1)] for row in range(length)]
        for i in range(1,length):
            diff=prices[i] - prices[i - 1]
            for j in range(1,k+1):
                local[i][j] = max(glob[i - 1][j - 1]+max(0 , diff), local[i-1][j] + diff)
                glob[i][j] = max(glob[i-1][j], local[i][j])

        return glob[length-1][k]





k=2
prices=[1,2,4,2,5,7,2,4,9,0]
a=Solution()
b=a.maxProfit(k,prices)
print b