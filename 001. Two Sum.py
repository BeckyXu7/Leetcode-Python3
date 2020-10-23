# Topic: Array
# 1. Two Sum - Easy

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# Method 1
# double for loop, faster than 20%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i, j in enumerate(nums):
            for k in range(i+1, length):
                if j + nums[k] == target:
                    return [i, k]

# Method 2
# Hashmap, faster than 98%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, j in enumerate(nums):
            if target - j in hashmap:
                return hashmap[target - j], i
            hashmap[j] = i
