class UnionTwoSort:
    """
    Print the union of two sorted arrays
    """

    def union(self, arr1, arr2):
        """
        Time Complexity: O(m +n)
        Space Complexity: O(1)
        :param arr1:
        :param arr2:
        :return:
        """
        i = j = 1
        last_print = -1
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                if last_print != arr1[i]:
                    print(arr1[i])
                    last_print = arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                if last_print != arr2[j]:
                    print(arr2[j])
                    last_print = arr2[j]
                j += 1
            else:
                print(arr2[j])
                i += 1
                j += 1
        while i < len(arr1):
            if arr1[i - 1] < arr1[i]:
                print(arr1[i])
            i += 1
        while j < len(arr2):
            if arr2[j - 1] < arr2[j]:
                print(arr2[j])
            j += 1


if __name__ == '__main__':
    test_arr_1 = [3, 5, 8, 15, 15]
    test_arr_2 = [2, 8, 9, 10, 10, 15]
    union = UnionTwoSort()
    union.union(test_arr_1, test_arr_2)
