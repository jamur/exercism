def is_valid_first_version(isbn):
    # test len
    scrubbed = [digit for digit in isbn if digit.isnumeric() or digit.isalpha()]
    if len(scrubbed) != 10:
        return False
    if not isbn[-1].isnumeric() and isbn[-1] != "X":
        return False
    if any(not digit.isnumeric() for digit in scrubbed[:-1]):
        return False
    list_digits = [int(digit) if digit.isnumeric() else 10
                   for digit in scrubbed]
    total = 0
    for counter, digit in enumerate(list_digits):
        total += int(digit) * (10 - counter)
    if total % 11 == 0:
        return True
    return False


print(is_valid("3-598-21508-8"))
print(is_valid("3132P34035"))