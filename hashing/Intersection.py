class Intersection:
    """
    Intersection class to find the intersection between elements of two array.
    """

    def intersection_array(self, nums1, nums2):
        """
        Time Complexity: O(m + n)
        Space Complexity: O(n)
        :param nums1:
        :param nums2:
        :return:
        """
        dic_num2 = {}
        for v in nums2:
            dic_num2[v] = v
        for v in nums1:
            if v in dic_num2:
                print(v)


if __name__ == "__main__":
    test_arr_1_1 = [10, 20, 30]
    test_arr_1_2 = [30, 10]
    intersection = Intersection()
    intersection.intersection_array(test_arr_1_1, test_arr_1_2)
