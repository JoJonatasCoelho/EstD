def consonants(string: str, consonants: int, vowels: int) -> bool:
    """
    Recursively checks if a string has more consonants than vowels.

    Args:
        string (str): The input string to check.
        consonants (int): The current count of consonants.
        vowels (int): The current count of vowels.

    Returns:
        bool: True if the number of consonants is greater than the number of vowels, False otherwise.
    """
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    if len(string) == 0:
        return consonants > vowels
    if string[0].lower() in vowels_list:
        return consonants(string[1:], consonants, vowels + 1)
    return consonants(string[1:], consonants + 1, vowels)

if __name__ == "__main__":
    print(consonants("abacaxi", 0, 0))