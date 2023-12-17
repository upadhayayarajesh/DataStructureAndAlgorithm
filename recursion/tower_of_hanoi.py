def tower_of_hanoi(n, A, B, C):
    """
    Steps require moving disk N for A to C using the bottom top approach.
    Time complexity: O(2^n)
    Space complexity: O(2^n)
    :param n: Number of disk in the source tower (A)
    :param A: Source tower
    :param B: Auxiliary tower
    :param C: Destination tower
    :return: None
    """
    if n == 1:
        print(f"{n} Move disk from {A} to {C}")
        return
    tower_of_hanoi(n - 1, A, C, B)
    print(f"Moved disk {n} from {A} to {C}")
    tower_of_hanoi(n - 1, B, A, C)


if __name__ == "__main__":
    tower_of_hanoi(4, "A", "B", "C")
