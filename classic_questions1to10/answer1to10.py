import collections
from random import random
from typing import List


class Solution:
    # 移除元素
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all instances of `val` in `nums` in-place and return the new length of the array.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k    
    # 移除重复元素
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove all duplicates in `nums` in-place and return the new length of the array.
        """
        k = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
    # 多数元素
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find the majority element in `nums`.
        """
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
    # 多数元素1
    def majorityElement1(self, nums: list[int]) -> int:
        """
        Find the majority element in `nums`.
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        print(k)
        print(nums[-k:])
        print(nums[:-k])
        nums[:] = nums[-k:] + nums[:-k]
        return nums
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find the maximum profit that can be achieved from `prices`.
        """
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        """
        Find the maximum profit that can be achieved from `prices`.
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
    
    def canJump(self, nums: List[int]) -> bool:
        """
        Determine if you can reach the last index of `nums`.
        """
        # max_reachable = 0
        # for i, jump in enumerate(nums):
        #     print(i, jump, max_reachable)
        #     if i > max_reachable:
        #         return False
        #     max_reachable = max(max_reachable, i + jump)
        # return True
        # 解法二 计算两个相邻数之差，如果前一个数大于后一个数，则跳跃长度增加差值，如果相等且不为0，则跳跃长度加1，否则跳跃长度增加前一个数与后一个数的差值，最后判断跳跃长度是否大于等于数组长度减1
        jump_length = 0
        for i in range(1,len(nums) - 1):
            if nums[i] > nums[i-1]:
                jump_length += nums[i]-nums[i-1]
            elif nums[i] == nums[i-1] and nums[i] != 0 and nums[i-1] != 0:
                jump_length += 1
            else:
                jump_length += nums[i-1]-nums[i]
        if jump_length >= len(nums) - 1:
            return True
        else:
            return False

    def jump(self, nums: List[int]) -> int:
        """
        Find the minimum number of jumps to reach the last index of `nums`.
        """
        # 跳跃次数
        jumps = 0
        current_end = 0
        # 当前index能跳跃的最远距离
        farthest = 0
        # 遍历数组，除了最后一个元素，因为最后一个元素是目标，不需要跳跃
        for i in range(len(nums) - 1):
        # 更新max_reach，记录当前index+i能跳跃的最远距离
            farthest = max(farthest, i + nums[i])
           # 如果当前index等于current_end，说明当前index是一个跳跃点，需要跳跃，数组自身保证了一定能到达最后一个元素
            if i == current_end:
                jumps += 1
                # 更新current_end，记录下一个跳跃点的最远距离
                current_end = farthest
        return jumps


    def hIndex(self, citations: List[int]) -> int:
        """
        Calculate the h-index from `citations`.
        """
        # 论文总数
        n = len(citations)
        # 创建桶
        buckets = [0] * (n + 1)
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
        count = 0
        for i in range(n, -1, -1):
            count += buckets[i]
            if count >= i:
                return i
        return 0
    
class RandomizedSet:
    """ RandomizedSet data structure that supports insert, remove, and getRandom operations in average O(1) time. """

    def __init__(self): 
        """
        Initialize your data structure here.
        """
        self.num_to_index = {}
        self.nums = []

        

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False
        self.num_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

        
        

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False
        index = self.num_to_index[val]
        last_element = self.nums[-1]
        self.nums[index] = last_element
        self.num_to_index[last_element] = index
        self.nums.pop()
        del self.num_to_index[val]
        return True


    def getRandom(self) -> int:
        return self.nums[int(random() * len(self.nums))]
