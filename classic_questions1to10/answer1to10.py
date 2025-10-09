import collections


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
    def majorityElement1(self, nums: List[int]) -> int:
        """
        Find the majority element in `nums`.
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)