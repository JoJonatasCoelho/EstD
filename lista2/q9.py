def greater_last(list: list[int], target: int) -> list[int]:
    """Returns a new list with the values greater than the target at the end.
                       
    Args:
        list (list[int]): List of integers.
        target (int): The target integer.

    Returns:
        list[int]: A new list with the values greater than the target at the end.
    """
    if len(list) == 0:
        return []
    if len(list) == 1:
        return list
    previous_list = greater_last(list[:-1], target)
    if list[-1] > target:
        previous_list.append(list[-1])
    elif list[-1] <= target:
        previous_list.insert(0, list[-1])
    return previous_list

if __name__ == "__main__":
    print(greater_last([1, 2, 3, 4, 5, 6, 8, 1, 2, 3], 4))
