def odd_last(list: list[int]) -> list[int]:
    """Returns a the pair values first in the list.
                       
    Args:
        list (list[int]): List of integers.

    Returns:
        list[int]: A new list with the odd numbers in last.
    """
    if len(list) == 0:
        return []
    if len(list) == 1:
        return list
    previous_list = odd_last(list[:-1])
    if list[-1] % 2:
        previous_list.insert(0, list[-1])
    return previous_list

if __name__ == "__main__":
    print(odd_last([1, 2, 3, 4, 5]))
