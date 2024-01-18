class Count_distinct:
    """
    Count distinct element in an array.
    """

    def Count_distinct(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param nums: Array to have distinct element in it.
        """
        dictionary = {}
        for v in nums:
            dictionary[v] = v
        return len(dictionary)


if __name__ == '__main__':
    test_arr_1 = [15, 12, 13, 12, 13, 13, 18]
    print(Count_distinct().Count_distinct(test_arr_1))
