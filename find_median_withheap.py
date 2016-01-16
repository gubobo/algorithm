import heapq
import sys

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minHeap=[]
        self.maxHeap=[]




    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.maxHeap)==len(self.minHeap):
            heapq.heappush(self.maxHeap,-heapq.heappushpop(self.minHeap,num))
        else:
            heapq.heappush(self.minHeap,-heapq.heappushpop(self.maxHeap,-num))



    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.maxHeap)==len(self.minHeap):
            return (-self.maxHeap[0]+self.minHeap[0])/2.0
        else:
            return -self.maxHeap[0]

mf = MedianFinder()
mf.addNum(1)
mf.addNum(3)
mf.addNum(2)
print mf.findMedian()