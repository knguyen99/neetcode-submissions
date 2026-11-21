import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        heap = []

        for num in counts:
            if len(heap) == k:
                heapq.heappushpop(heap, [counts[num], num])
            else:
                heapq.heappush(heap, [counts[num], num])
        return [i[1] for i in heap]