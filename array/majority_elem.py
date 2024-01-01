def majority_element_1(arr):
    """
    Find the majority element in array.
    Majority element means the element needs to appear more than len(arr) / 2 times.
    Time complexity: O(N ^2)
    Space complexity: O(N)
    :param arr: Array
    :return: Index of majority element or -1
    """
    for i, v in enumerate(arr):
        count = 1
        for j in range(i + 1, len(arr)):
            if arr[j] == v:
                count += 1
            if count > len(arr) / 2:
                return j
    return -1


if __name__ == '__main__':
    test_arr_1 = [8, 3, 4, 8, 8]  # O/P = 0 or 2 or 3
    test_arr_2 = [6, 8, 4, 8, 8]  # O/p = 1 or 3  or 4

    print(majority_element_1(test_arr_1))
    print(majority_element_1(test_arr_2))
