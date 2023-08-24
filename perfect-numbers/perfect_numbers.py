def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    # sum factors
    total = sum(n for n in
                range(1, number // 2 + 1) # half is enough
                if not number % n)
    # classify
    if total == number:
        return "perfect"
    if total > number:
        return "abundant"
    return "deficient"
