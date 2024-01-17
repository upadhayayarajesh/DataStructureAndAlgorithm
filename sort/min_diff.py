class MinDiff:
    """
    Minimum difference between two element in an array.
    """

    def min_diff_arr(self, nums):
        """
        Time Complexity: O(n * log(n))
        Space Complexity: o(1)
        :param nums: Array of number
        :return: minimum difference between elements in nums
        """
        nums.sort()
        print(nums)
        res = float('inf')
        for i in range(1, len(nums)):
            res = min(res, nums[i] - nums[i - 1])
        return res


if __name__ == '__main__':
    nums = [1, 8, 12, 5, 18]
    print(MinDiff().min_diff_arr(nums))
