class FrequencyCount:
    """
    Frequency count of an element in an array.
    """

    def frequency_count(self, nums):
        """
        Time complexity :O(n)
        Space complexity :O(n)
        :param nums: Element to be found in the array.
        :return: None
        """
        frequencies_count = {}
        for v in nums:
            if v in frequencies_count.keys():
                frequencies_count[v] = frequencies_count[v] + 1
            else:
                frequencies_count[v] = 1
        for key, value in frequencies_count.items():
            print(key, value)


if __name__ == '__main__':
    test_arr_1 = [10, 12, 10, 15, 10, 20, 10, 12, 12]
    FrequencyCount().frequency_count(test_arr_1)
