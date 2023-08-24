def steps2(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    total = 0
    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        total += 1
    return total

def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    return 0 if number == 1 else \
        1 + steps(number // 2 if number % 2 == 0 else number * 3 + 1)
    # return 0 if number == 1 else \
    #     1 + (steps(number // 2) if number % 2 == 0 else steps(number * 3 + 1))