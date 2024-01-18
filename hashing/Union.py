class Union:
    """
    Union of elements in two array.
    """

    def union_two_arr(self, nums1, nums2):
        """
        Time Complexity: O(n +m)
        Space Complexity: O(n + m)
        :param nums1: Array
        :param nums2: Array
        :return: None
        """
        dic = {}
        for v in nums1:
            dic[v] = v
        for v in nums2:
            dic[v] = v
        for key in dic.keys():
            print(key)


if __name__ == '__main__':
    test_arr_1 = [10, 30, 10]
    test_arr_2 = [5, 10, 5]
    union = Union()
    union.union_two_arr(test_arr_1, test_arr_2)
