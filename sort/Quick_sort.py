class QuickSort:
    """
    Divide and conquer Algorithm
    Worst case time complexity: O(n^2)
    Despite O(n^2) worst case, it is considered faster because:
    1. In-Place algorithm
    2. Average time complexity: O(nlog(n))
    3. Tail Recursive
    Partition is the key function (naive, Lomuto, Hoare)
    Stable in Naive approach but unstable in Lomuto approach and Hoarse approach
    """

    def lomuto_partition(self, arr, low, high):
        pivot = arr[high]  # Choose the last element as the pivot
        i = low - 1  # Index of smaller element

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap elements

        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in its correct position
        return i + 1  # Return the pivot index

    def quick_sort_lomuto(self, nums, l, h):
        if l < h:
            p = self.lomuto_partition(nums, l, h)
            self.quick_sort_lomuto(nums, l, p - 1)
            self.quick_sort_lomuto(nums, p + 1, h)


if __name__ == '__main__':
    test_arr_1 = [8, 4, 7, 9, 3, 10, 5]
    quick_sort = QuickSort()
    quick_sort.quick_sort_lomuto(test_arr_1, 0, len(test_arr_1) - 1)
    print(test_arr_1)
