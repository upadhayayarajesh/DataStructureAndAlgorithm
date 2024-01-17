class SortArrayThreeTypes:
    """
    Sorts array with three types of given middle types.
    keeps one together in a sorted array.
    This question is same to keep the elements of a range together in a sorted array.
    """

    def SortArrayThreeTypes(self, nums):
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:  Array of 0, 1, 2
        :return: Sorted array with all the ones together
        """
        lo = 0
        hi = len(nums) - 1
        mid = 0
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[hi], nums[mid] = nums[mid], nums[hi]
                hi -= 1
        return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 2, 1, 2]
    print(SortArrayThreeTypes().SortArrayThreeTypes(nums, 1))
