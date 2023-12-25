# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            sum.append(current_sum)
        return sum