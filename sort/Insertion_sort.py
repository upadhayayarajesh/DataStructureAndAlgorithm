class Insertion_sort:
    """
    Insertion sort is an in-place and stable sorting algorithm
    Mostly using in small sized array.
    """

    def insertion(self, arr):
        """
        Time Complexity: O(n ^ 2)
        Space Complexity: O(1)
        :param arr: Array to be sorted
        :return: Sorted array
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


if __name__ == '__main__':
    test_arr_1 = [20, 5, 40, 60, 10, 30]
    insertion_sort = Insertion_sort()
    print(insertion_sort.insertion(test_arr_1))
