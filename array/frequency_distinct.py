def frequency_distinct(arr):
    """
    Find the frequency of each element and print it with the element in a sorted array
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Sorted array
    :return: None
    """
    current_frequency = 0
    curr_num = arr[0]
    for i, v in enumerate(arr):
        if v == curr_num:
            current_frequency += 1
        else:
            print(f"{curr_num} appears {current_frequency}")
            curr_num = v
            current_frequency = 1
    print(f"{curr_num} appears {current_frequency}")


if __name__ == "__main__":
    arr_test_1 = [10, 10, 10, 25, 30, 30]
    arr_test_2 = [10, 10, 10, 10]
    arr_test_3 = [10, 20, 30]

    frequency_distinct(arr_test_1)
    frequency_distinct(arr_test_2)
    frequency_distinct(arr_test_3)
