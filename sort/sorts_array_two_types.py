class SortArrayTwoTypes:
    """
    Sorts the array order doesn't matter based on given type postive one side and negative another side,
    """

    def sort_array_two_types(self, nums):
        """
         Time implementation: O(N)
         Space implementation: O(1)
        :param nums: Array to be sorted based on the given array.
        :return: Sorted array based on the given element.
        """
        pivot = 0
        j = -1
        for i in range(len(nums)):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    nums = [15, -3, -2, 18]
    print(SortArrayTwoTypes().sort_array_two_types(nums))
