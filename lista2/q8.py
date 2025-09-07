def two_sum_recursive(arr: list[int], target: int, left: int, right: int) -> bool:
    """
    Recursively checks if there is a pair of elements in a sorted list whose sum equals the target value.

    Args:
        arr (list[int]): Sorted list of integers.
        target (int): Target sum value.
        left (int): Starting index for the search.
        right (int): Ending index for the search.

    Returns:
        bool: True if there is a pair whose sum equals the target, False otherwise.
    """
    if left >= right:
        return False
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        return True
    elif current_sum < target:
        return two_sum_recursive(arr, target, left + 1, right)
    else:
        return two_sum_recursive(arr, target, left, right - 1)
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 10
    print(two_sum_recursive(arr, target, 0, len(arr) - 1)) 
    target = 19
    print(two_sum_recursive(arr, target, 0, len(arr) - 1))