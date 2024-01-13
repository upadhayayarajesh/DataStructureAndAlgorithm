from typing import List


class Repeating_element:
    """
    Repeating element in an array where
    There are all the elements present less that max of array from zero.
    """

    def repeating_1(self, arr: List[int]):
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param arr:
        :return:
        """
        visited = [False] * len(arr)
        for v in arr:
            if visited[v]:
                return v
            visited[v] = True


if __name__ == '__main__':
    test_arr_1 = [0, 2, 1, 3, 2, 2]
    test_arr_2 = [0, 0]
    repeating_elem = Repeating_element()
    print(repeating_elem.repeating_1(test_arr_1))
    print(repeating_elem.repeating_1(test_arr_2))
