class Partition:
    """"
    Do a partition of an array around a given index of the array
    """

    def partition_native(self, nums, p):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        temp = []
        for v in nums:
            if v <= nums[p]:
                temp.append(v)
        for v in nums:
            if v > nums[p]:
                temp.append(v)
        for i, v in enumerate(temp):
            nums[i] = v
        return nums

    def partition_lomuto(self, nums, l, h):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        lower_window_start = -1
        pivot = nums[-1]
        for i in range(l, h - 1):
            if nums[i] < pivot:
                nums[i], nums[lower_window_start + 1] = nums[lower_window_start + 1], nums[i]
                lower_window_start += 1
        return nums

    def partition_hoare(self, nums, l, h):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        pivot = nums[0]
        i = l - 1
        j = h + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1
            j -= 1
            while nums[j] > pivot:
                j -= 1
            if i >= j:
                return nums
            nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    test_arr_1 = [10, 80, 30, 90, 40, 50, 70]
    partition = Partition()
    print(partition.partition_native(test_arr_1, 6))
    print(partition.partition_lomuto(test_arr_1, 0,7))
    test_arr_2 = [5, 3, 8, 4, 2, 7, 1, 10]
    print(partition.partition_hoare(test_arr_2, 0, 7))
