class PairSum:
    """
    find a pair in an array such that it's sum is equal to the s
    """

    def pair_sum(self, nums, s):
        dict = {}
        for v in nums:
            elem = s - v
            if elem in dict.keys():
                return True
            else:
                dict[v] = v
        return False


if __name__ == '__main__':
    test_arr_1 = [8, 3, 4, 2, 5]
    print(PairSum().pair_sum(test_arr_1, 6))
