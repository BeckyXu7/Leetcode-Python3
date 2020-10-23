# Topic: HashTable
# 136. Simple Number - Easy

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:

Input: nums = [2,2,1]
Output: 1
'''

# Method 1
# use Counter, faster than 38%
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i, j in c.items():
            if j == 1:
                return i

# Method
# use ^, faster than 38%
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        for j in nums:
            i = i^j
        return i
