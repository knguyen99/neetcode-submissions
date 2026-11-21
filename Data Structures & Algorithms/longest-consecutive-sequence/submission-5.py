import bisect
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0

        for num in nums:
            if num + 1 not in nums:
                curr = 0
                currnum = num
                while currnum in nums:
                    curr += 1
                    ans = max(curr, ans)
                    currnum -= 1
        return ans
