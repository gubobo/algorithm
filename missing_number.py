#ecoding:utf-8
#其他解法,可以参考https://leetcode.com/problems/missing-number/
import sys
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = sys.maxint
        max = -sys.maxint
        sum=0

        for a in nums:
            if a > max:
                max = a
            if a<min:
                min = a
            sum += a

        missing = (max+min)*(max-min+1)/2-sum
        if missing == 0:
            if min == 1:
                return min-1
            if min == 0:
                return max+1

        return missing




a=Solution()
b=[0,1]
print a.missingNumber(b)