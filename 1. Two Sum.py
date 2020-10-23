# Topic: Array
# 1. Two Sum - Easy

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
