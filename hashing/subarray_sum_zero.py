class Subarray:
    """
    Checks if there is a subarray with sum zero
    """

    def is_subarray_zero(self, nums):
        """
        Checks if there is a subarray with sum zero
        Time complexity: O(N)
        Space complexity: O(N)
        :param nums: Array of numbers
        :return: Boolean
        """
        prefix_sum = {}
        s = 0
        for v in nums:
            s += v
            if s in prefix_sum.keys():
                return True
            if s == 0:
                return True
            prefix_sum[v] = s
        return False


if __name__ == '__main__':
    test_arr_1 = [-3, 4, -3, -1, 1]
    print(Subarray().is_subarray_zero(test_arr_1))
