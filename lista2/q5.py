def greaterDigit(number: int) -> int:
    if number < 10:
        return number
    last = number % 10
    return max(last, greaterDigit(number // 10))

def smallerDigit(number: int) -> int:
    if number < 10:
        return number
    last = number % 10
    return min(last, smallerDigit(number // 10))

def countDigits(number: int) -> int:
    if number < 10:
        return 1
    return 1 + countDigits(number // 10)

def sumDigits(number: int) -> int:
    if number < 10:
        return number
    last = number % 10
    return last + sumDigits(number // 10)

def zeroEvens(number: int) -> int:
    if number < 10:
        return number if number % 2 == 1 else 0
    last = number % 10
    return 10 * zeroEvens(number // 10) + (last if last % 2 == 1 else 0)

def zeroOdds(number: int) -> int:
    if number < 10:
        return number if number % 2 == 0 else 0
    last = number % 10
    return 10 * zeroOdds(number // 10) + (last if last % 2 == 0 else 0)

def removePairs(number: int) -> int:
    if number < 10:
        return number if number % 2 == 1 else 0
    last = number % 10
    return removePairs(number // 10) * 10 + last if last % 2 == 1 else removePairs(number // 10) 

def removeOdds(number: int) -> int:
    if number < 10:
        return number if number % 2 == 0 else 0
    last = number % 10
    return removeOdds(number // 10) * 10 + last if last % 2 == 0 else removeOdds(number // 10)

def invertNumber(number: int) -> int:
    def helper(number: int, inverted: int) -> int:
        if number == 0:
            return inverted
        last = number % 10
        inverted = inverted * 10 + last
        return helper(number // 10, inverted)
    return helper(number, 0)

if __name__ == "__main__":
    print(greaterDigit(12394567))
    print(smallerDigit(1234567))
    print(countDigits(1234567))
    print(sumDigits(1234567))
    print(zeroEvens(1234567))
    print(zeroOdds(1234567))
    print(removePairs(1234567))
    print(removeOdds(1234567))
    print(invertNumber(1234567))