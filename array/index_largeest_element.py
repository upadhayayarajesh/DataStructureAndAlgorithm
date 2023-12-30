def index_largest_element(arr):
    """
    This function is used to find the largest element in array
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array
    :return: Index of the largest element present in an array
    """
    largest_index = 0
    for i, v in enumerate(arr):
        if v > arr[largest_index]:
            largest_index = i
    return largest_index


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(index_largest_element(arr))
