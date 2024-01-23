class CountDistinctEveryWin:
    """
    You are given an array and a number k, you need to print the distinct elements
    in every window of the array.
    The total number of  possible windows is given by n -k +1, where n is number of element in an array.
    """

    def count_distinct_elem_every_win(self, nums1, K):
        """
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param nums1: An integer array
        :param K: window size
        :return:None
        """
        total_win = len(nums1) - K + 1
        for i in range(total_win):
            count_dis = {}
            for j in range(i, i + K):
                count_dis[nums1[j]] = nums1[j]
            print(len(count_dis))

    def count_distinct_elem_every_win_effective(self, nums1, K):
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        hash_table = {}
        start = 0
        end = 0
        while end < len(nums1):
            if hash_table.get(nums1[end]):
                hash_table[nums1[end]] = hash_table[nums1[end]] + 1
            else:
                hash_table[nums1[end]] = 1
            if end - start == K - 1:
                print(len(hash_table))

                hash_table[nums1[start]] = hash_table[nums1[start]] - 1
                if hash_table[nums1[start]] == 0:
                    hash_table.pop(nums1[start])
                start += 1
            end += 1


if __name__ == '__main__':
    test_arr_1 = [10, 20, 20, 10, 30, 40, 10]
    CountDistinctEveryWin().count_distinct_elem_every_win(test_arr_1, 4)
    CountDistinctEveryWin().count_distinct_elem_every_win_effective(test_arr_1, 4)
