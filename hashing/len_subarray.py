class LenCommonSubarray:
    """
    Given two binary sub array you need to find the length of the common index on the sub array
    with equal sum.
    """

    def len_common_subarray_1(self, nums1, nums2):
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param nums1: A binary array
        :param nums2: A binary array
        :return: len the largest common sub array with equal sum.
        """
        res = 0
        for i in range(len(nums1)):
            nums1_sum = nums1[i]
            nums2_sum = nums2[i]
            for j in range(i + 1, len(nums2)):
                nums1_sum += nums1[j]
                nums2_sum += nums2[j]
                if nums1_sum == nums2_sum:
                    res = max(res, (j - i + 1))
        return res

    def len_common_subarray_2(self, nums1, num2):
        """
         Time Complexity: O(n)
         Space Complexity: O(n)
        """
        temp = []
        for i in range(len(nums1)):
            temp.append(nums1[i] - num2[i])
        prefix_sum = {}
        pre = 0
        res = 0
        for i in range(len(temp)):
            pre += temp[i]
            if pre in prefix_sum.keys():
                res = max(res, i - prefix_sum[pre])
                continue
            if pre == 0:
                res = max(res, i)
            prefix_sum[pre] = i
        return res


if __name__ == '__main__':
    test_arra_1_1 = [0, 1, 0, 0, 0, 0]
    test_arra_1_2 = [1, 0, 1, 0, 0, 1]
    print(LenCommonSubarray().len_common_subarray_1(test_arra_1_1, test_arra_1_2))
    print(LenCommonSubarray().len_common_subarray_2(test_arra_1_1, test_arra_1_2))
