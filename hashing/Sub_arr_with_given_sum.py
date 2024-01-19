class Sub_arr_with_given_sum:
    """
    Check if there is a sub array with given sum in an array.
    """

    def sub_arr_sum(self, nums, s):
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums: list of integers
        :param s: sum of numbers
        :return: Boolean
        """""
        prefix_sum = {}
        pre = 0
        for v in nums:
            pre += v
            if pre in prefix_sum.keys():
                return True
            t = pre + s
            prefix_sum[t] = t

        return False


if __name__ == '__main__':
    nums = [5, 8, 6, 13, 3, -1]
    print(Sub_arr_with_given_sum().sub_arr_sum(nums, 22))
