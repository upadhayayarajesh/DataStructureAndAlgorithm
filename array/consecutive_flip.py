def consecutive_flip(arr):
    """
    Minimum number of flips required to make the binary string of only one element.
    Idea come as thew max difference of 0 and i group is either 0 and 1.
    which make us that minimum group is second group.
    Time complexity = O(N)
    Space complexity = O(1)
    :param arr: Binary array
    :return: None
    """

    pre = arr[0]
    for i, v in enumerate(arr):
        if v != pre:
            if v != arr[0]:
                print(f"From {i} to ")
            else:
                print(i - 1)
            pre = v


if __name__ == "__main__":
    test_arr_1 = [0, 0, 1, 1, 0, 0, 1, 1, 0]
    consecutive_flip(test_arr_1)
