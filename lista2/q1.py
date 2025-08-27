def greater(list: list[int]) -> int:
    """Returns the greatest number in a list of integers recursively.

    Args:
        list (list[int]): List of integers.

    Returns:
        int: The greatest number in the list.
    """
    if len(list) == 0:
        raise ValueError("The list cannot be empty.")
    if len(list) == 1:
        return list[0]
    greatest = greater(list[:-1])
    return greatest if greatest > list[-1] else list[-1]

if __name__ == "__main__":
    print(greater([3, 5, 2, 9, 1]))
    print([3, 5, 2, 9, 1][:-1])