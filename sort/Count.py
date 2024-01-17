class Count:
    """
    Counting sorting algorithm.
    It works in linear time if the element range is less than n number of element
    """

    def Counting_sort(self, nums, k):
        """
        Time Complexity: O(n + K)
        Space Complexity: O(K)
        It only works with number but if they represent the object it doesn't work.
        :param nums:
        :param k:
        :return:
        """
        nums2 = [0] * k
        for v in nums:
            nums2[v] = nums2[v] + 1
        print(nums2)
        counter = 0
        for i, v in enumerate(nums2):
            curr = v
            while curr > 0:
                nums[counter] = i
                curr -= 1
                counter += 1
        return nums

    def Counting_sort_object(self, nums, k):
        """
        Time Complexity: O(n + K)
        Space Complexity: O(n + k)
        It works with number and also if they represent the object too.
        :param nums:
        :param k:
        :return:
        """
        nums2 = [0] * k
        for v in nums:
            nums2[v] = nums2[v] + 1

        for i in range(1, len(nums2)):
            nums2[i] = nums2[i] + nums2[i - 1]

        output = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            t = nums[i]
            nums2[t] = nums2[t] - 1
            output[nums2[t]] = nums[i]
        for i, v in enumerate(output):
            nums[i] = v
        return nums


if __name__ == '__main__':
    test_nums = [1, 4, 4, 1, 0, 1]
    count_obj = Count()
    count_obj.Counting_sort_object(test_nums, 5)
    print(test_nums)
