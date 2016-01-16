#295. Find Median from Data Stream

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data=[]
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        self.data.append(num)
        length=len(self.data)

        if length>1:
            j=length-2
            while j>=0 and num < self.data[j]:
                self.data[j+1]=self.data[j]
                j-=1
            self.data[j+1]=num
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        length=len(self.data)
        if length%2!=0:
            return self.data[length/2]
        else:
            return (self.data[length/2-1]+self.data[length/2])/2

#
# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(3)
mf.addNum(2)
a=mf.findMedian()
print a