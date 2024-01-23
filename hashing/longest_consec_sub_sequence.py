class LongestConsecSubSequence:
    """
     Length of longest consecutive sub-sequence array
    """

    def longest_consec_sub_sequence(self, num1):
        """
        Time Complexity: O(n log(n))
        Space Complexity: O(1)
        :param num1:
        :return:
        """
        num1.sort()
        cons = 1
        res = 1
        for i in range(1, len(num1)):
            if num1[i] - num1[i - 1] == 1:
                cons += 1
            else:
                res = max(res, cons)
                cons = 1
        return res

    def longest_consecutive_sub_seq_eff(self, nums1):
        hash = {}
        res = 1
        for num in nums1:
            hash[num] = num

        for v in nums1:
            if v - 1 in hash.keys():
                continue
            else:
                count = 1
                while v + 1 in hash.keys():
                    count += 1
                    v += 1
                res = max(res, count)
        return res


if __name__ == '__main__':
    test_arr_1 = [1, 9, 3, 4, 2, 10]
    test_arr_2 = [8, 20, 7, 30]
    print(LongestConsecSubSequence().longest_consec_sub_sequence(test_arr_1))
    print(LongestConsecSubSequence().longest_consecutive_sub_seq_eff(test_arr_2))
