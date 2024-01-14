class Intersection:
    """
    Print the intersection element on both the sorted array.
    """

    def intersection(self, nums1, nums2):
        """
        Time complexity: O(m +n)
        Space complexity: O(1)
        :param nums1:
        :param nums2:
        :return:
        """
        i = j = k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                print(nums1[i], nums2[j])
                i += 1
                j += 1


if __name__ == '__main__':
    test_arr_1 = [3, 5, 10, 10, 10, 15, 15, 20]
    test_arr_2 = [5, 10, 10, 15, 30]
    intersection = Intersection()
    intersection.intersection(test_arr_1, test_arr_2)
