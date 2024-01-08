def triplet_sorted_array_1(arr, x):
    """
       True or False if a sum of triplet is equal to x
       Time complexity: O(N^3)
       Space complexity: O(1)
       :param x: Inger sum
       :param arr: Sorted array
       :return: Boolean value
       """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == x:
                    return True
    return False


def triplet_sorted_array_2(arr, x):
    """
        True or False if a sum of triplet is equal to x
        Time complexity: O(N^2)
        Space complexity: O(1)
        :param x: Inger sum
        :param arr: Sorted array
        :return: Boolean value
   """
    low, high = 0, len(arr) - 1
    while low < high:
        if arr[low] + arr[high] >= x:
            high -= 1
        if arr[low] + arr[high] < x:
            for i in range(low + 1, high):
                if arr[low] + arr[high] + arr[i] == x:
                    return True
            low += 1
    return False


if __name__ == '__main__':
    test_arr_1 = [2, 3, 4, 8, 9, 20, 40]
    print(triplet_sorted_array_1(test_arr_1, 32))
    print(triplet_sorted_array_2(test_arr_1, 32))
