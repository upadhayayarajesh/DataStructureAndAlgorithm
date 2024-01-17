class MergeOverlapInterval:
    """
    Sorted merge overlap interval
    """

    def merge(self, nums):
        """
        Time complexity: O(N)
        Space complexity: O(1)
        :param nums:
        :return:
        """
        current_range = nums[0]
        for i in range(1, len(nums)):
            if current_range[1] > nums[i][0]:
                current_range[0] = min(current_range[0], nums[i][0])
                current_range[1] = max(current_range[1], nums[i][1])

            else:
                print(current_range)
                current_range = nums[i]
        print(current_range)


if __name__ == '__main__':
    test_arr_1 = [[1, 3], [2, 4], [5, 7], [6, 8]]
    MergeOverlapInterval().merge(test_arr_1)
