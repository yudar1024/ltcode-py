from typing import List

class Solution11to20:
    """
    11. 除自身以外数组的乘积
    12. Integer to Roman
    13. Roman to Integer
    14. Longest Common Prefix
    15. 3Sum
    16. 3Sum Closest
    17. Letter Combinations of a Phone Number
    18. 4Sum
    19. Remove Nth Node From End of List
    20. Valid Parentheses
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        11. 除自身以外数组的乘积，不要使用除法，且在 O(n) 时间复杂度内完成此题。
        示例 1:
        输入: nums = [1,2,3,4]
        输出: [24,12,8,6]
        """
        n = len(nums)
        res = [1] * n
        # 计算左侧乘积
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        print(res)
        right = nums[-1]
        for i in range(n-2, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res