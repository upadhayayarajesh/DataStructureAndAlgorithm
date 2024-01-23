class Longest:
    """
    Find the longest subarray with the same number of zero and one's in a binary array.
    """

    def longest_naive(self, nums):
        """
        :return:
        """
        curr_max = 0
        for i in range(len(nums)):
            one = 0
            zero = 0
            for d in range(i, len(nums)):
                if nums[d] == 0:
                    zero += 1
                else:
                    one += 1
                if one == zero:
                    curr_max = max(curr_max, (one + zero))
        return curr_max

    def longest_efficienct(self, nums):
        for i, v in enumerate(nums):
            if v == 0:
                nums[i] = -1
        prefix_sum = {}
        pre = 0
        res = 0
        for i, v in enumerate(nums):
            pre += v
            if pre in prefix_sum.keys():
                res = max(res, (i - prefix_sum[pre]))
                continue
            if pre == 0:
                res = max(res, i + 1)
            prefix_sum[pre] = i
        return res


if __name__ == '__main__':
    test_arr_1 = [1, 0, 1, 1, 1, 0, 0]
    test_arr_2 = [1, 1, 0, 1]
    print(Longest().longest_efficienct(test_arr_2))
