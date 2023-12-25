# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        largest_wealth = 0
        for account in accounts:
            if sum(account) > largest_wealth:
                largest_wealth = sum(account)
        return largest_wealth