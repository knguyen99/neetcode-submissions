from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        window = deque()
        for i in range(k):
            while window and window[-1][0] < nums[i]:
                window.pop()
            window.append((nums[i],i))
        
        ret.append(window[0][0])

        for i in range(k,len(nums)):
            while window and window[0][1] <= i - k:
                window.popleft()

            while window and window[-1][0] < nums[i]:
                window.pop()
            
            window.append((nums[i],i))
            ret.append(window[0][0])
        return ret
