def factors(value):
    return list(factors_generator(value))

def factors_generator(value):
    divisor = 2
    while divisor <= value:
        if value % divisor == 0:
            yield divisor
            value //= divisor
        else:
            divisor += 1

# this doesn't pass on large factors test
# because exceed maximum recursion depth
def factors_generator_recursive(value, divisor=2):
    if value <= 1:
        return
    if value % divisor == 0:
        yield divisor
        yield from factors_generator_recursive(value // divisor, divisor)
    else:
        yield from factors_generator_recursive(value, divisor + 1)

