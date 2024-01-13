from typing import List


class Median_two_sorted_arr:
    """
    Given a two sorted integer arrays nums1 and nums2
    Find the median of the two sorted integers.
    """

    def median_1(self, nums1: List[int], nums2: List[int]):
        """
        :param nums1: A list of integers
        :param nums2: A list of integers
        Time Complexity: O(m + n)
        Space Complexity: O(m + n)
        :return: Median of the two sorted arrays
        """
        result = []
        n1 = 0
        n2 = 0
        counter = 0
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] > nums2[n2]:
                result.append(nums2[n2])
                n2 += 1
            else:
                result.append(nums1[n1])
                n1 += 1
            counter += 1
        if n1 < len(nums1):
            while n1 < len(nums1):
                result.append(nums1[n1])
                n1 += 1
        if n2 < len(nums2):
            while n2 < len(nums2):
                result.append(nums2[n2])
                nums2 += 1

        mid = int(len(result) / 2)
        if len(result) % 2 == 0:
            return (result[mid] + result[mid - 1]) / 2
        return result[mid]


if __name__ == '__main__':
    test_arr_1_1 = [10, 20, 30, 40, 50]
    test_arr_1_2 = [5, 15, 25, 35, 45]
    med_sort = Median_two_sorted_arr()
    print(med_sort.median_1(test_arr_1_1, test_arr_1_2))
