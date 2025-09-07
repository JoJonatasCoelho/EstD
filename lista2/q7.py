def binary_search(array: list[int], target: int, low: int, high: int) -> bool:
    """
    Recursively performs binary search to determine if a target value exists in a sorted list.

    Args:
        array (list[int]): Sorted list of integers to search.
        target (int): The value to search for.
        low (int): The starting index of the search range.
        high (int): The ending index of the search range.

    Returns:
        bool: True if the target is found in the array, False otherwise.
    """
    if low > high:
        return False
    mid = (low + high) // 2
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, high)
    else:
        return binary_search(array, target, low, mid - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
    target = 5
    print(binary_search(arr, target, 0, len(arr) - 1)) 
    target = 10
    print(binary_search(arr, target, 0, len(arr) - 1)) 