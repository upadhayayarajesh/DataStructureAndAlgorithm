def remove_dup_sorted_arr(arr):
    """
    It removes the duplicates from the sorted array.
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array
    :return: Array without duplicates and length of a distinct element in the array.
    """
    start = 1
    for i in range(1, len(arr)):
        if arr[start - 1] != arr[i]:
            arr[start] = arr[i]
            start += 1
    return [arr, start]


if __name__ == "__main__":
    test_arr_1 = [10, 20, 20, 30, 30, 30, 30]
    test_arr_2 = [10, 10, 10, ]
    test_arr_3 = [10, 20, 20, 30, 30, 50, 50, 60, 70]

    print(remove_dup_sorted_arr(test_arr_1))
    print(remove_dup_sorted_arr(test_arr_2))
    print(remove_dup_sorted_arr(test_arr_3))
